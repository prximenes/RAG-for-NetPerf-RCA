#!/usr/bin/env python3
"""
Módulo de limpeza de texto para RAG Dataset Builder.

Copiado do projeto principal para manter este artefato autocontido.
"""

# NOTE: conteúdo idêntico ao `rag-application/dataset/text_cleaner.py` (sem dependências externas).

import re
import logging
from typing import List, Dict, Any
from collections import Counter

logger = logging.getLogger(__name__)


class TextCleaner:
    def __init__(
        self,
        aggressive: bool = False,
        remove_line_breaks: bool = True,
        fix_hyphenation: bool = True,
        remove_page_numbers: bool = True,
        remove_headers_footers: bool = True,
        normalize_whitespace: bool = True,
        normalize_punctuation: bool = True,
        remove_control_chars: bool = True,
        min_line_length: int = 0,
        preserve_urls: bool = True,
        preserve_emails: bool = True,
        verbose: bool = False,
    ):
        self.aggressive = aggressive
        self.remove_line_breaks = remove_line_breaks
        self.fix_hyphenation = fix_hyphenation
        self.remove_page_numbers = remove_page_numbers
        self.remove_headers_footers = remove_headers_footers
        self.normalize_whitespace = normalize_whitespace
        self.normalize_punctuation = normalize_punctuation
        self.remove_control_chars = remove_control_chars
        self.min_line_length = min_line_length
        self.preserve_urls = preserve_urls
        self.preserve_emails = preserve_emails
        self.verbose = verbose
        self._compile_patterns()

    def _compile_patterns(self):
        self.url_pattern = re.compile(
            r'https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b'
            r'(?:[-a-zA-Z0-9()@:%_\+.~#?&/=]*)'
        )
        self.email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        self.page_number_pattern = re.compile(
            r'^\s*(?:p[aá]gina|page|pg\.?|p\.?)?\s*\d+\s*$',
            re.IGNORECASE | re.MULTILINE,
        )
        self.hyphen_pattern = re.compile(r'(\w+)-\s*\n\s*(\w+)')
        self.multi_space_pattern = re.compile(r' {2,}')
        self.multi_newline_pattern = re.compile(r'\n{3,}')
        self.duplicate_punct_pattern = re.compile(r'([.!?;,:]){2,}')
        self.control_chars_pattern = re.compile(r'[\x00-\x08\x0b-\x0c\x0e-\x1f\x7f-\x9f]')
        self.citation_pattern = re.compile(r'\[\d+\]|\(\d{4}\)|\bet al\.')

    def clean(self, text: str, track_changes: bool = False):
        if not text or not isinstance(text, str):
            return text

        original_length = len(text)
        changes: Dict[str, Any] = {}

        protected_items: Dict[str, str] = {}
        if self.preserve_urls:
            text, protected_items = self._protect_patterns(text, self.url_pattern, protected_items, "URL")
        if self.preserve_emails:
            text, protected_items = self._protect_patterns(text, self.email_pattern, protected_items, "EMAIL")

        if self.remove_control_chars:
            before = len(text)
            text = self.control_chars_pattern.sub("", text)
            changes["control_chars_removed"] = before - len(text)

        if self.fix_hyphenation:
            before = text.count("-\n")
            text = self.hyphen_pattern.sub(r"\1\2", text)
            changes["hyphenation_fixed"] = before - text.count("-\n")

        if self.remove_page_numbers:
            lines_before = len(text.split("\n"))
            text = self.page_number_pattern.sub("", text)
            changes["page_numbers_removed"] = lines_before - len(text.split("\n"))

        if self.remove_headers_footers:
            text, removed = self._remove_repeated_lines(text)
            changes["repeated_lines_removed"] = removed

        if self.remove_line_breaks:
            text = self._smart_line_break_removal(text)

        if self.normalize_punctuation:
            before = len(re.findall(self.duplicate_punct_pattern, text))
            text = self.duplicate_punct_pattern.sub(r"\1", text)
            changes["duplicate_punctuation_normalized"] = before

        if self.normalize_whitespace:
            text = self.multi_space_pattern.sub(" ", text)
            text = self.multi_newline_pattern.sub("\n\n", text)
            text = "\n".join(line.strip() for line in text.split("\n"))

        if self.min_line_length > 0:
            lines = text.split("\n")
            filtered = [line for line in lines if len(line.strip()) >= self.min_line_length or len(line.strip()) == 0]
            changes["short_lines_removed"] = len(lines) - len(filtered)
            text = "\n".join(filtered)

        if self.aggressive:
            text = self._aggressive_clean(text)

        text = self._restore_protected(text, protected_items)
        text = text.strip()

        changes["total_chars_removed"] = original_length - len(text)
        changes["compression_ratio"] = f"{(1 - len(text)/original_length)*100:.1f}%" if original_length > 0 else "0%"

        if self.verbose:
            self._log_changes(changes)

        if track_changes:
            return text, changes
        return text

    def clean_texts(self, texts: List[str], show_progress: bool = False) -> List[str]:
        cleaned = []
        total = len(texts)
        for i, text in enumerate(texts):
            cleaned.append(self.clean(text))
            if show_progress and (i + 1) % 100 == 0:
                logger.info("Limpeza: %s/%s textos processados", i + 1, total)
        return cleaned

    def _protect_patterns(self, text: str, pattern: re.Pattern, protected: Dict[str, str], prefix: str):
        matches = pattern.findall(text)
        for i, match in enumerate(matches):
            placeholder = f"__{prefix}_{i}__"
            protected[placeholder] = match
            text = text.replace(match, placeholder, 1)
        return text, protected

    def _restore_protected(self, text: str, protected: Dict[str, str]) -> str:
        for placeholder, original in protected.items():
            text = text.replace(placeholder, original)
        return text

    def _smart_line_break_removal(self, text: str) -> str:
        lines = text.split("\n")
        result: List[str] = []
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if not line:
                if result and result[-1] != "":
                    result.append("")
                i += 1
                continue
            if self._is_special_line(line):
                result.append(line)
                i += 1
                continue
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                if not next_line:
                    result.append(line)
                    i += 1
                    continue
                if line and line[-1] not in ".!?:;":
                    result.append(line + " " + next_line)
                    i += 2
                    continue
            result.append(line)
            i += 1
        return "\n\n".join(result)

    def _is_special_line(self, line: str) -> bool:
        if re.match(r"^\s*[\d\-\•\*]\s+", line):
            return True
        if len(line) < 80 and line.isupper():
            return True
        if self.citation_pattern.search(line):
            return True
        return False

    def _remove_repeated_lines(self, text: str, threshold: int = 3):
        lines = text.split("\n")
        line_counts = Counter()
        for line in lines:
            stripped = line.strip()
            if stripped and len(stripped) > 5:
                line_counts[stripped] += 1
        repeated = {line for line, count in line_counts.items() if count >= threshold}
        filtered: List[str] = []
        removed = 0
        for line in lines:
            if line.strip() in repeated:
                removed += 1
            else:
                filtered.append(line)
        return "\n".join(filtered), removed

    def _aggressive_clean(self, text: str) -> str:
        text = text.encode("ascii", "ignore").decode("ascii")
        lines = text.split("\n")
        filtered = [line for line in lines if not re.match(r"^[\d\W]+$", line.strip()) or len(line.strip()) == 0]
        return "\n".join(filtered)

    def _log_changes(self, changes: Dict[str, Any]):
        logger.info("Estatísticas de limpeza:")
        for key, value in changes.items():
            if isinstance(value, int) and value > 0:
                logger.info(" - %s: %s", key, value)
            elif isinstance(value, str):
                logger.info(" - %s: %s", key, value)


_default_cleaner = TextCleaner()
_aggressive_cleaner = TextCleaner(aggressive=True)


def clean_text(text: str, aggressive: bool = False, track_changes: bool = False, **kwargs):
    if kwargs:
        cleaner = TextCleaner(aggressive=aggressive, **kwargs)
        return cleaner.clean(text, track_changes=track_changes)
    cleaner = _aggressive_cleaner if aggressive else _default_cleaner
    return cleaner.clean(text, track_changes=track_changes)


def clean_texts(texts: List[str], aggressive: bool = False, show_progress: bool = False, **kwargs) -> List[str]:
    if kwargs:
        cleaner = TextCleaner(aggressive=aggressive, **kwargs)
        return cleaner.clean_texts(texts, show_progress=show_progress)
    cleaner = _aggressive_cleaner if aggressive else _default_cleaner
    return cleaner.clean_texts(texts, show_progress=show_progress)


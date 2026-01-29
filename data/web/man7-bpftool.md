---
                {
  "source": "web",
  "label": "man7-bpftool",
  "url": "https://man.archlinux.org/man/bpftool.8.en",
  "description": "bpftool reference for eBPF/XDP inspection and profiling",
  "license": null,
  "collected_at": "2025-12-15T17:15:20.398944+00:00"
}
                ---
                # bpftool(8) — Linux manual page

                bpftool(8) — Arch manual pagesArch Linux
- Home
- Packages
- Forums
- Wiki
- GitLab
- Security
- AUR
- Download
BPFTOOL(8)System Manager's ManualBPFTOOL(8)
NAME
BPFTOOL - tool for inspection and simple manipulation of eBPF
    programs and maps
SYNOPSIS
bpftool [OPTIONS] OBJECT { COMMAND |
    help }
bpftoolbatch fileFILE
bpftoolversion
OBJECT := { map | prog | link |
    cgroup | perf | net | feature | btf |
    gen | struct_ops | iter }
OPTIONS := { { -V | --version } | { -j
    | --json } [{ -p | --pretty }] | { -d |
    --debug } }
MAP-COMMANDS := { show | list | create
    | dump | update | lookup | getnext |
    delete | pin | event_pipe | help }
PROG-COMMANDS := { show | list | dump
    jited | dump xlated | pin | load | attach |
    detach | help }
LINK-COMMANDS := { show | list | pin |
    detach | help }
CGROUP-COMMANDS := { show | list |
    attach | detach | help }
PERF-COMMANDS := { show | list | help
    }
NET-COMMANDS := { show | list | help
  }
FEATURE-COMMANDS := { probe | help }
BTF-COMMANDS := { show | list | dump |
    help }
GEN-COMMANDS := { object | skeleton |
    min_core_btf | help }
STRUCT-OPS-COMMANDS := { show | list |
    dump | register | unregister | help }
ITER-COMMANDS := { pin | help }
DESCRIPTION
bpftool allows for inspection and simple modification of
    BPF objects on the system.
Note that format of the output of all tools is not guaranteed to
    be stable and should not be depended upon.
OPTIONS
-h,
    --helpPrint short help message (similar to bpftool help).-V,
    --versionPrint bpftool's version number (similar to bpftool version), the
      number of the libbpf version in use, and optional features that were
      included when bpftool was compiled. Optional features include linking
      against LLVM or libbfd to provide the disassembler for JIT-ted programs
      (bpftool progdump jited) and usage of BPF skeletons (some
      features like bpftool progprofile or showing pids
      associated to BPF objects may rely on it).-j,
    --jsonGenerate JSON output. For commands that cannot produce JSON, this option
      has no effect.-p,
    --prettyGenerate human-readable JSON output. Implies -j.-d,
    --debugPrint all logs available, even debug-level information. This includes logs
      from libbpf as well as from the verifier, when attempting to load
      programs.
-m,
    --mapcompatAllow loading maps with unknown map definitions.-n,
    --nomountDo not automatically attempt to mount any virtual file system (such as
      tracefs or BPF virtual file system) when necessary.
SEE   ALSO
bpf(2), bpf-helpers(7), bpftool-btf(8),
    bpftool-cgroup(8), bpftool-feature(8), bpftool-gen(8),
    bpftool-iter(8), bpftool-link(8), bpftool-map(8),
    bpftool-net(8), bpftool-perf(8), bpftool-prog(8),
    bpftool-struct_ops(8)
Package information:
Package name:extra/bpfVersion:6.17-2Upstream:https://www.kernel.orgLicenses:GPL-2.0-onlyManuals:/listing/extra/bpf/
Table of contents
- NAME
- SYNOPSIS
- DESCRIPTION
- OPTIONS
- SEE ALSO
Other formats:
            txt,
            raw
Powered by archmanweb,
               using mandoc for the conversion of manual pages.
The website is available under the terms of the GPL-3.0
               license, except for the contents of the manual pages, which have their own license
               specified in the corresponding Arch Linux package.

---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/system/target-loongarch.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.279110+00:00"
}
                    ---
                    # docs/system/target-loongarch.rst

                    .. _LoongArch-System-emulator:

LoongArch System emulator
-------------------------

QEMU can emulate loongArch 64 bit systems via the
``qemu-system-loongarch64`` binary. Only one machine type ``virt`` is
supported.

When using KVM as accelerator, QEMU can emulate la464 cpu model. And when
using the default cpu model with TCG as accelerator, QEMU will emulate a
subset of la464 cpu features that should be enough to run distributions
built for the la464.

Board-specific documentation
============================

.. toctree::
   loongarch/virt

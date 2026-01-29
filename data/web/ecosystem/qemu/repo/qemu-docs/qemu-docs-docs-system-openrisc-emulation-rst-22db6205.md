---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/system/openrisc/emulation.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.339615+00:00"
}
                    ---
                    # docs/system/openrisc/emulation.rst

                    OpenRISC 1000 CPU architecture support
======================================

QEMU's TCG emulation includes support for the OpenRISC or1200 implementation of
the OpenRISC 1000 cpu architecture.

The or1200 cpu also has support for the following instruction subsets:

- ORBIS32 (OpenRISC Basic Instruction Set)
- ORFPX32 (OpenRISC Floating-Point eXtension)

In addition to the instruction subsets the QEMU TCG emulation also has support
for most Class II (optional) instructions.

For information on all OpenRISC instructions please refer to the latest
architecture manual available on the OpenRISC website in the
`OpenRISC Architecture <https://openrisc.io/architecture>`_ section.

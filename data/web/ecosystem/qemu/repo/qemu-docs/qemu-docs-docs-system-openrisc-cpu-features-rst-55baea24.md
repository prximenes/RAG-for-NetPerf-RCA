---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/system/openrisc/cpu-features.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.339047+00:00"
}
                    ---
                    # docs/system/openrisc/cpu-features.rst

                    CPU Features
============

The QEMU emulation of the OpenRISC architecture provides following built in
features.

- Shadow GPRs
- MMU TLB with 128 entries, 1 way
- Power Management (PM)
- Programmable Interrupt Controller (PIC)
- Tick Timer

These features are on by default and the presence can be confirmed by checking
the contents of the Unit Presence Register (``UPR``) and CPU Configuration
Register (``CPUCFGR``).

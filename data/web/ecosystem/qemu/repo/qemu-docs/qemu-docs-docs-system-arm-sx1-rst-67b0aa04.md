---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/system/arm/sx1.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.340241+00:00"
}
                    ---
                    # docs/system/arm/sx1.rst

                    Siemens SX1 (``sx1``, ``sx1-v1``)
=================================

The Siemens SX1 models v1 and v2 (default) basic emulation. The
emulation includes the following elements:

-  Texas Instruments OMAP310 System-on-chip (ARM925T core)

-  ROM and RAM memories (ROM firmware image can be loaded with
   -pflash) V1 1 Flash of 16MB and 1 Flash of 8MB V2 1 Flash of 32MB

-  On-chip LCD controller

-  On-chip Real Time Clock

-  Secure Digital card connected to OMAP MMC/SD host

-  Three on-chip UARTs

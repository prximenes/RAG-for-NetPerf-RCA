---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/system/arm/musca.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.353473+00:00"
}
                    ---
                    # docs/system/arm/musca.rst

                    Arm Musca boards (``musca-a``, ``musca-b1``)
============================================

The Arm Musca development boards are a reference implementation
of a system using the SSE-200 Subsystem for Embedded. They are
dual Cortex-M33 systems.

QEMU provides models of the A and B1 variants of this board.

Unimplemented devices:

- SPI
- |I2C|
- |I2S|
- PWM
- QSPI
- Timer
- SCC
- GPIO
- eFlash
- MHU
- PVT
- SDIO
- CryptoCell

Note that (like the real hardware) the Musca-A machine is
asymmetric: CPU 0 does not have the FPU or DSP extensions,
but CPU 1 does. Also like the real hardware, the memory maps
for the A and B1 variants differ significantly, so guest
software must be built for the right variant.

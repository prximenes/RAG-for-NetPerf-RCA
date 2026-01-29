---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/system/arm/highbank.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.347651+00:00"
}
                    ---
                    # docs/system/arm/highbank.rst

                    Calxeda Highbank and Midway (``highbank``, ``midway``)
======================================================

``highbank`` is a model of the Calxeda Highbank (ECX-1000) system,
which has four Cortex-A9 cores.

``midway`` is a model of the Calxeda Midway (ECX-2000) system,
which has four Cortex-A15 cores.

Emulated devices:

- L2x0 cache controller
- SP804 dual timer
- PL011 UART
- PL061 GPIOs
- PL031 RTC
- PL022 synchronous serial port controller
- AHCI
- XGMAC ethernet controllers

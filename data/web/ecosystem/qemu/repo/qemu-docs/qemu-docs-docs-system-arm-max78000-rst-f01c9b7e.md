---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/system/arm/max78000.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.341891+00:00"
}
                    ---
                    # docs/system/arm/max78000.rst

                    .. SPDX-License-Identifier: GPL-2.0-or-later

Analog Devices max78000 board (``max78000fthr``)
================================================

The max78000 is a Cortex-M4 based SOC with a RISC-V coprocessor. The RISC-V coprocessor is not supported.

Supported devices
-----------------

 * Instruction Cache Controller
 * UART
 * Global Control Register
 * True Random Number Generator
 * AES

Notable unsupported devices
---------------------------

 * I2C
 * CNN
 * CRC
 * SPI

Boot options
------------

The max78000 can be started using the ``-kernel`` option to load a
firmware at address 0 as the ROM. As the ROM normally jumps to software loaded
from the internal flash at address 0x10000000, loading your program there is
generally advisable. If you don't have a copy of the ROM, the interrupt
vector table from user firmware will do.
Example:

.. code-block:: bash

  $ qemu-system-arm -machine max78000fthr -kernel max78000.bin -device loader,file=max78000.bin,addr=0x10000000

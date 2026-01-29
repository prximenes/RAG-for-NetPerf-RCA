---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/system/riscv/xiangshan-kunminghu.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.332261+00:00"
}
                    ---
                    # docs/system/riscv/xiangshan-kunminghu.rst

                    BOSC Xiangshan Kunminghu FPGA prototype platform (``xiangshan-kunminghu``)
==========================================================================
The ``xiangshan-kunminghu`` machine is compatible with our FPGA prototype
platform.

XiangShan is an open-source high-performance RISC-V processor project.
The third generation processor is called Kunminghu. Kunminghu is a 64-bit
RV64GCBSUHV processor core. More information can be found in our Github
repository:
https://github.com/OpenXiangShan/XiangShan

Supported devices
-----------------
The ``xiangshan-kunminghu`` machine supports the following devices:

* Up to 16 xiangshan-kunminghu cores
* Core Local Interruptor (CLINT)
* Incoming MSI Controller (IMSIC)
* Advanced Platform-Level Interrupt Controller (APLIC)
* 1 UART

Boot options
------------
The ``xiangshan-kunminghu`` machine can start using the standard ``-bios``
functionality for loading the boot image. You need to compile and link
the firmware, kernel, and Device Tree (FDT) into a single binary file,
such as ``fw_payload.bin``.

Running
-------
Below is an example command line for running the ``xiangshan-kunminghu``
machine:

.. code-block:: bash

   $ qemu-system-riscv64 -machine xiangshan-kunminghu \
      -smp 16 -m 16G \
      -bios path/to/opensbi/platform/generic/firmware/fw_payload.bin \
      -nographic

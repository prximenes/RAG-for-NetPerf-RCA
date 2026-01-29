---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/system/arm/xlnx-zynq.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.343859+00:00"
}
                    ---
                    # docs/system/arm/xlnx-zynq.rst

                    Xilinx Zynq board (``xilinx-zynq-a9``)
======================================
The Zynq 7000 family is based on the AMD SoC architecture. These products
integrate a feature-rich dual or single-core Arm Cortex-A9 MPCore based
processing system (PS) and AMD programmable logic (PL) in a single device.

More details here:
https://docs.amd.com/r/en-US/ug585-zynq-7000-SoC-TRM/Zynq-7000-SoC-Technical-Reference-Manual

QEMU xilinx-zynq-a9 board supports following devices:
    - A9 MPCORE
        - cortex-a9
        - GIC v1
        - Generic timer
        - wdt
    - OCM 256KB
    - SMC SRAM@0xe2000000 64MB
    - Zynq SLCR
    - SPI x2
    - QSPI
    - UART
    - TTC x2
    - Gigabit Ethernet Controller x2
    - SD Controller x2
    - XADC
    - Arm PrimeCell DMA Controller
    - DDR Memory
    - USB 2.0 x2

Running
"""""""
Direct Linux boot of a generic ARM upstream Linux kernel:

.. code-block:: bash

  $ qemu-system-aarch64 -M xilinx-zynq-a9 \
        -dtb zynq-zc702.dtb  -serial null -serial mon:stdio \
        -display none  -m 1024 \
        -initrd rootfs.cpio.gz -kernel zImage

For configuring the boot-mode provide the following on the command line:

.. code-block:: bash

   -machine boot-mode=qspi

Supported values are jtag, sd, qspi, nor.

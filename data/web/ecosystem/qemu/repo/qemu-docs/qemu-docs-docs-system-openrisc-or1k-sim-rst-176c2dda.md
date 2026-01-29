---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/system/openrisc/or1k-sim.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.339893+00:00"
}
                    ---
                    # docs/system/openrisc/or1k-sim.rst

                    Or1ksim board
=============

The QEMU Or1ksim machine emulates the standard OpenRISC board simulator which is
also the standard SoC configuration.

Supported devices
-----------------

 * 16550A UART
 * ETHOC Ethernet controller
 * SMP (OpenRISC multicore using ompic)

Boot options
------------

The Or1ksim machine can be started using the ``-kernel`` and ``-initrd`` options
to load a Linux kernel and optional disk image.

.. code-block:: bash

  $ qemu-system-or1k -cpu or1220 -M or1k-sim -nographic \
        -kernel vmlinux \
        -initrd initramfs.cpio.gz \
        -m 128

Linux guest kernel configuration
""""""""""""""""""""""""""""""""

The 'or1ksim_defconfig' for Linux openrisc kernels includes the right
drivers for the or1ksim machine.  If you would like to run an SMP system
choose the 'simple_smp_defconfig' config.

Hardware configuration information
""""""""""""""""""""""""""""""""""

The ``or1k-sim`` board automatically generates a device tree blob ("dtb")
which it passes to the guest. This provides information about the
addresses, interrupt lines and other configuration of the various devices
in the system.

The location of the DTB will be passed in register ``r3`` to the guest operating
system.

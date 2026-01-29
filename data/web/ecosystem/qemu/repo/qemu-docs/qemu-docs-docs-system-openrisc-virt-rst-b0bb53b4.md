---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/system/openrisc/virt.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.339321+00:00"
}
                    ---
                    # docs/system/openrisc/virt.rst

                    'virt' generic virtual platform
===============================

The ``virt`` board is a platform which does not correspond to any
real hardware; it is designed for use in virtual machines.
It is the recommended board type if you simply want to run
a guest such as Linux and do not care about reproducing the
idiosyncrasies and limitations of a particular bit of real-world
hardware.

Supported devices
-----------------

 * PCI/PCIe devices
 * 8 virtio-mmio transport devices
 * 16550A UART
 * Goldfish RTC
 * SiFive Test device for poweroff and reboot
 * SMP (OpenRISC multicore using ompic)

Boot options
------------

The virt machine can be started using the ``-kernel`` and ``-initrd`` options
to load a Linux kernel and optional disk image. For example:

.. code-block:: bash

  $ qemu-system-or1k -cpu or1220 -M or1k-sim -nographic \
        -device virtio-net-device,netdev=user -netdev user,id=user,net=10.9.0.1/24,host=10.9.0.100 \
        -device virtio-blk-device,drive=d0 -drive file=virt.qcow2,id=d0,if=none,format=qcow2 \
        -kernel vmlinux \
        -initrd initramfs.cpio.gz \
        -m 128

Linux guest kernel configuration
""""""""""""""""""""""""""""""""

The 'virt_defconfig' for Linux openrisc kernels includes the right drivers for
the ``virt`` machine.

Hardware configuration information
""""""""""""""""""""""""""""""""""

The ``virt`` board automatically generates a device tree blob ("dtb") which it
passes to the guest. This provides information about the addresses, interrupt
lines and other configuration of the various devices in the system.

The location of the DTB will be passed in register ``r3`` to the guest operating
system.

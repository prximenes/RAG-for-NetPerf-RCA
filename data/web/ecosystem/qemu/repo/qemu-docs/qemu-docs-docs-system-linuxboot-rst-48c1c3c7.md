---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/system/linuxboot.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.281740+00:00"
}
                    ---
                    # docs/system/linuxboot.rst

                    .. _direct_005flinux_005fboot:

Direct Linux Boot
-----------------

This section explains how to launch a Linux kernel inside QEMU without
having to make a full bootable image. It is very useful for fast Linux
kernel testing.

The syntax is:

.. parsed-literal::

   |qemu_system| -kernel bzImage -drive file=rootdisk.img,format=raw -append "root=/dev/sda"

Use ``-kernel`` to provide the Linux kernel image and ``-append`` to
give the kernel command line arguments. The ``-initrd`` option can be
used to provide an INITRD image.

If you do not need graphical output, you can disable it and redirect the
virtual serial port and the QEMU monitor to the console with the
``-nographic`` option. The typical command line is:

.. parsed-literal::

   |qemu_system| -kernel bzImage -drive file=rootdisk.img,format=raw \
                    -append "root=/dev/sda console=ttyS0" -nographic

Use :kbd:`Ctrl+a c` to switch between the serial console and the monitor (see
:ref:`GUI_keys`).

---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/system/monitor.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.272169+00:00"
}
                    ---
                    # docs/system/monitor.rst

                    .. _QEMU monitor:

QEMU Monitor
------------

The QEMU monitor is used to give complex commands to the QEMU emulator.
You can use it to:

-  Remove or insert removable media images (such as CD-ROM or
   floppies).

-  Freeze/unfreeze the Virtual Machine (VM) and save or restore its
   state from a disk file.

-  Inspect the VM state without an external debugger.

Commands
~~~~~~~~

The following commands are available:

.. hxtool-doc:: hmp-commands.hx

.. hxtool-doc:: hmp-commands-info.hx

Integer expressions
~~~~~~~~~~~~~~~~~~~

The monitor understands integers expressions for every integer argument.
You can use register names to get the value of specifics CPU registers
by prefixing them with *$*.

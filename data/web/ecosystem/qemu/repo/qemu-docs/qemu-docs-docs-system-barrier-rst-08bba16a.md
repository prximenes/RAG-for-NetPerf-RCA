---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/system/barrier.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.283066+00:00"
}
                    ---
                    # docs/system/barrier.rst

                    QEMU Barrier Client
===================

Generally, mouse and keyboard are grabbed through the QEMU video
interface emulation.

But when we want to use a video graphic adapter via a PCI passthrough
there is no way to provide the keyboard and mouse inputs to the VM
except by plugging a second set of mouse and keyboard to the host
or by installing a KVM software in the guest OS.

The QEMU Barrier client avoids this by implementing directly the Barrier
protocol into QEMU.

`Barrier <https://github.com/debauchee/barrier>`__
is a KVM (Keyboard-Video-Mouse) software forked from Symless's
synergy 1.9 codebase.

This protocol is enabled by adding an input-barrier object to QEMU.

Syntax::

    input-barrier,id=<object-id>,name=<guest display name>
    [,server=<barrier server address>][,port=<barrier server port>]
    [,x-origin=<x-origin>][,y-origin=<y-origin>]
    [,width=<width>][,height=<height>]

The object can be added on the QEMU command line, for instance with::

    -object input-barrier,id=barrier0,name=VM-1

where VM-1 is the name the display configured in the Barrier server
on the host providing the mouse and the keyboard events.

by default ``<barrier server address>`` is ``localhost``,
``<port>`` is ``24800``, ``<x-origin>`` and ``<y-origin>`` are set to ``0``,
``<width>`` and ``<height>`` to ``1920`` and ``1080``.

If the Barrier server is stopped QEMU needs to be reconnected manually,
by removing and re-adding the input-barrier object, for instance
with the help of the HMP monitor::

    (qemu) object_del barrier0
    (qemu) object_add input-barrier,id=barrier0,name=VM-1

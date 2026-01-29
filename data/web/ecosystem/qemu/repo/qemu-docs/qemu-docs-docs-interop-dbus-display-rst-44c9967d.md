---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/interop/dbus-display.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.248956+00:00"
}
                    ---
                    # docs/interop/dbus-display.rst

                    D-Bus display
=============

QEMU can export the VM display through D-Bus (when started with ``-display
dbus``), to allow out-of-process UIs, remote protocol servers or other
interactive display usages.

Various specialized D-Bus interfaces are available on different object paths
under ``/org/qemu/Display1/``, depending on the VM configuration.

QEMU also implements the standard interfaces, such as
`org.freedesktop.DBus.Introspectable
<https://dbus.freedesktop.org/doc/dbus-specification.html#standard-interfaces>`_.

.. contents::
   :local:
   :depth: 1

.. only:: sphinx4

   .. dbus-doc:: ui/dbus-display1.xml

.. only:: not sphinx4

   .. warning::
      Sphinx 4 is required to build D-Bus documentation.

      This is the content of ``ui/dbus-display1.xml``:

   .. literalinclude:: ../../ui/dbus-display1.xml
      :language: xml

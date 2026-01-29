---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/interop/dbus-vmstate.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.240233+00:00"
}
                    ---
                    # docs/interop/dbus-vmstate.rst

                    =============
D-Bus VMState
=============

The QEMU dbus-vmstate object's aim is to migrate helpers' data running
on a QEMU D-Bus bus. (refer to the :doc:`dbus` document for
some recommendations on D-Bus usage)

Upon migration, QEMU will go through the queue of
``org.qemu.VMState1`` D-Bus name owners and query their ``Id``. It
must be unique among the helpers.

It will then save arbitrary data of each Id to be transferred in the
migration stream and restored/loaded at the corresponding destination
helper.

For now, the data amount to be transferred is arbitrarily limited to
1Mb. The state must be saved quickly (a fraction of a second). (D-Bus
imposes a time limit on reply anyway, and migration would fail if data
isn't given quickly enough.)

dbus-vmstate object can be configured with the expected list of
helpers by setting its ``id-list`` property, with a comma-separated
``Id`` list.

.. only:: sphinx4

   .. dbus-doc:: backends/dbus-vmstate1.xml

.. only:: not sphinx4

   .. warning::
      Sphinx 4 is required to build D-Bus documentation.

      This is the content of ``backends/dbus-vmstate1.xml``:

   .. literalinclude:: ../../backends/dbus-vmstate1.xml
      :language: xml

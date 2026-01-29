---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/system/target-s390x.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.287737+00:00"
}
                    ---
                    # docs/system/target-s390x.rst

                    .. _s390x-System-emulator:

s390x System emulator
---------------------

QEMU can emulate z/Architecture (in particular, 64 bit) s390x systems
via the ``qemu-system-s390x`` binary. Only one machine type,
``s390-ccw-virtio``, is supported (with versioning for compatibility
handling).

When using KVM as accelerator, QEMU can emulate CPUs up to the generation
of the host. When using the default cpu model with TCG as accelerator,
QEMU will emulate a subset of z13 cpu features that should be enough to run
distributions built for the z13.

Device support
==============

QEMU will not emulate most of the traditional devices found under LPAR or
z/VM; virtio devices (especially using virtio-ccw) make up the bulk of
the available devices. Passthrough of host devices via vfio-pci, vfio-ccw,
or vfio-ap is also available.

.. toctree::
   s390x/vfio-ap
   s390x/css
   s390x/3270
   s390x/vfio-ccw
   s390x/pcidevices

Architectural features
======================

.. toctree::
   s390x/bootdevices
   s390x/protvirt
   s390x/cpu-topology

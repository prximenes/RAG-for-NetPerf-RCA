---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/system/devices/virtio/index.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.361812+00:00"
}
                    ---
                    # docs/system/devices/virtio/index.rst

                    VirtIO Devices
==============

VirtIO devices are paravirtualized devices designed to be efficient to
emulate and virtualize. Unless you are specifically trying to exercise
a driver for some particular hardware they are the recommended device
models to use for virtual machines.

The `VirtIO specification`_ is an open standard managed by OASIS. It
describes how a *driver* in a guest operating system interacts with
the *device* model provided by QEMU. Multiple Operating Systems
support drivers for VirtIO with Linux perhaps having the widest range
of device types supported.

The device implementation can either be provided wholly by QEMU, or in
concert with the kernel (known as *vhost*). The device implementation
can also be off-loaded to an external process via :ref:`vhost user
<vhost_user>`.

.. toctree::
   :maxdepth: 1

   virtio-gpu.rst
   virtio-pmem.rst
   virtio-snd.rst
   vhost-user.rst
   vhost-user-contrib.rst

.. _VirtIO specification: https://docs.oasis-open.org/virtio/virtio/v1.3/virtio-v1.3.html

---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/system/target-i386.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.286411+00:00"
}
                    ---
                    # docs/system/target-i386.rst

                    .. _QEMU-PC-System-emulator:

x86 System emulator
-------------------

Board-specific documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

..
   This table of contents should be kept sorted alphabetically
   by the title text of each file, which isn't the same ordering
   as an alphabetical sort by filename.

.. toctree::
   :maxdepth: 1

   i386/pc
   i386/microvm
   i386/nitro-enclave

Architectural features
~~~~~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 1

   i386/cpu
   i386/hyperv
   i386/xen
   i386/xenpvh
   i386/kvm-pv
   i386/sgx
   i386/amd-memory-encryption
   i386/tdx

OS requirements
~~~~~~~~~~~~~~~

On x86_64 hosts, the default set of CPU features enabled by the KVM
accelerator require the host to be running Linux v4.5 or newer.

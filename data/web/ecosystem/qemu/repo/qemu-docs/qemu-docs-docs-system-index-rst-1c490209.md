---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/system/index.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.283795+00:00"
}
                    ---
                    # docs/system/index.rst

                    .. _System Emulation:

----------------
System Emulation
----------------

This section of the manual is the overall guide for users using QEMU
for full system emulation (as opposed to user-mode emulation).
This includes working with hypervisors such as KVM, Xen
or Hypervisor.Framework.

.. toctree::
   :maxdepth: 3

   introduction
   invocation
   device-emulation
   keys
   mux-chardev
   monitor
   images
   virtio-net-failover
   linuxboot
   generic-loader
   guest-loader
   barrier
   vnc-security
   tls
   secrets
   authz
   gdb
   replay
   managed-startup
   bootindex
   cpu-hotplug
   pr-manager
   targets
   security
   multi-process
   confidential-guest-support
   igvm
   vm-templating
   sriov

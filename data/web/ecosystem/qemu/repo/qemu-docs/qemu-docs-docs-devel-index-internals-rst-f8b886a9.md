---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/devel/index-internals.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.317464+00:00"
}
                    ---
                    # docs/devel/index-internals.rst

                    .. _internal-subsystem:

Internal Subsystem Information
------------------------------

Details about QEMU's various subsystems including how to add features to them.

.. toctree::
   :maxdepth: 2

   qom
   atomics
   rcu
   block-coroutine-wrapper
   clocks
   ebpf_rss
   migration/index
   multi-process
   reset
   s390-cpu-topology
   s390-dasd-ipl
   tracing
   uefi-vars
   vfio-iommufd
   writing-monitor-commands
   virtio-backends
   crypto
   multiple-iothreads

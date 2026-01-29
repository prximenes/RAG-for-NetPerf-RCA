---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/devel/index-tcg.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.318664+00:00"
}
                    ---
                    # docs/devel/index-tcg.rst

                    .. _tcg:

TCG Emulation
-------------

Details about QEMU's Tiny Code Generator and the infrastructure
associated with emulation. You do not need to worry about this if you
are only implementing things for HW accelerated hypervisors.

.. toctree::
   :maxdepth: 2

   tcg
   tcg-ops
   decodetree
   multi-thread-tcg
   tcg-icount
   tcg-plugins
   replay

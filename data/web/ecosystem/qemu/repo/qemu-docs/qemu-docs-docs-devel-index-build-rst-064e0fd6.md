---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/devel/index-build.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.302174+00:00"
}
                    ---
                    # docs/devel/index-build.rst

                    QEMU Build System
-----------------

Details about how QEMU's build system works. You will need to understand
some of the basics if you are adding new files and targets to the build.

.. toctree::
   :maxdepth: 3

   build-system
   build-environment
   kconfig
   docs
   qapi-code-gen
   qapi-domain
   control-flow-integrity

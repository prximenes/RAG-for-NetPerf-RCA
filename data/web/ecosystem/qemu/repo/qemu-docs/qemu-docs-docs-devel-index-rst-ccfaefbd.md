---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/devel/index.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.309850+00:00"
}
                    ---
                    # docs/devel/index.rst

                    ---------------------
Developer Information
---------------------

This section of the manual documents various parts of the internals of
QEMU. You only need to read it if you are interested in reading or
modifying QEMU's source code.

QEMU is a large and mature project with a number of complex subsystems
that can be overwhelming to understand. The development documentation
is not comprehensive but hopefully presents enough to get you started.
If there are areas that are unclear please reach out either via the
IRC channel or mailing list and hopefully we can improve the
documentation for future developers.

All developers will want to familiarise themselves with
:ref:`development_process` and how the community interacts. Please pay
particular attention to the :ref:`coding-style` and
:ref:`submitting-a-patch` sections to avoid common pitfalls.

If you wish to implement a new hardware model you will want to read
through the :ref:`qom` documentation to understand how QEMU's object
model works.

Those wishing to enhance or add new CPU emulation capabilities will
want to read our :ref:`tcg` documentation, especially the overview of
the :ref:`tcg_internals`.

.. toctree::
   :maxdepth: 1

   index-process
   index-build
   testing/index
   index-api
   index-internals
   index-tcg
   codebase

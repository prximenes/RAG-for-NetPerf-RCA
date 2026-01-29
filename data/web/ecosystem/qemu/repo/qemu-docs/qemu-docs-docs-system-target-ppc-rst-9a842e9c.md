---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/system/target-ppc.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.285475+00:00"
}
                    ---
                    # docs/system/target-ppc.rst

                    .. _PowerPC-System-emulator:

PowerPC System emulator
-----------------------

Board-specific documentation
============================

You can get a complete list by running ``qemu-system-ppc64 --machine
help``.

..
   This table of contents should be kept sorted alphabetically
   by the title text of each file, which isn't the same ordering
   as an alphabetical sort by filename.

.. toctree::
   :maxdepth: 1

   ppc/amigang
   ppc/embedded
   ppc/powermac
   ppc/powernv
   ppc/ppce500
   ppc/prep
   ppc/pseries

---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/system/arm/digic.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.349644+00:00"
}
                    ---
                    # docs/system/arm/digic.rst

                    Canon A1100 (``canon-a1100``)
=============================

This machine is a model of the Canon PowerShot A1100 camera, which
uses the DIGIC SoC. This model is based on reverse engineering efforts
by the contributors to the `CHDK <http://chdk.wikia.com/>`_ and
`Magic Lantern <http://www.magiclantern.fm/>`_ projects.

The emulation is incomplete. In particular it can't be used
to run the original camera firmware, but it can successfully run
an experimental version of the `barebox bootloader <http://www.barebox.org/>`_.

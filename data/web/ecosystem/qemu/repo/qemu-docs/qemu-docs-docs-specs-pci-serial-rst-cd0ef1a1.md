---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/specs/pci-serial.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.268627+00:00"
}
                    ---
                    # docs/specs/pci-serial.rst

                    =======================
QEMU PCI serial devices
=======================

QEMU implements some PCI serial devices which are simple PCI
wrappers around one or more 16550 UARTs.

There is one single-port variant and two multiport-variants.  Linux
guests work out-of-the box with all cards.  There is a Windows inf file
(``docs/qemupciserial.inf``) to set up the cards in Windows guests.


Single-port card
----------------

Name:
  ``pci-serial``
PCI ID:
  1b36:0002
PCI Region 0:
   IO bar, 8 bytes long, with the 16550 UART mapped to it.
Interrupt:
   Wired to pin A.


Multiport cards
---------------

Name:
  ``pci-serial-2x``, ``pci-serial-4x``
PCI ID:
  1b36:0003 (``-2x``) and 1b36:0004 (``-4x``)
PCI Region 0:
   IO bar, with two or four 16550 UARTs mapped after each other.
   The first is at offset 0, the second at offset 8, and so on.
Interrupt:
   Wired to pin A.

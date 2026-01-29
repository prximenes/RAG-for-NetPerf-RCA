---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/system/ppc/powermac.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.358186+00:00"
}
                    ---
                    # docs/system/ppc/powermac.rst

                    PowerMac family boards (``g3beige``, ``mac99``)
==================================================================

Use the executable ``qemu-system-ppc`` to simulate a complete PowerMac
PowerPC system.

- ``g3beige``              Heathrow based PowerMac
- ``mac99``                Mac99 based PowerMac

Supported devices
-----------------

QEMU emulates the following PowerMac peripherals:

 *  UniNorth or Grackle PCI Bridge
 *  PCI VGA compatible card with VESA Bochs Extensions
 *  2 PMAC IDE interfaces with hard disk and CD-ROM support
 *  NE2000 PCI adapters
 *  Non Volatile RAM
 *  VIA-CUDA with ADB keyboard and mouse.


Missing devices
---------------

 * To be identified

Firmware
--------

Since version 0.9.1, QEMU uses OpenBIOS https://www.openbios.org/ for
the g3beige and mac99 PowerMac and the 40p machines. OpenBIOS is a free
(GPL v2) portable firmware implementation. The goal is to implement a
100% IEEE 1275-1994 (referred to as Open Firmware) compliant firmware.

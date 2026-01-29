---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/specs/acpi_pci_hotplug.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.258492+00:00"
}
                    ---
                    # docs/specs/acpi_pci_hotplug.rst

                    QEMU<->ACPI BIOS PCI hotplug interface
======================================

QEMU supports PCI hotplug via ACPI, for PCI bus 0. This document
describes the interface between QEMU and the ACPI BIOS.

ACPI GPE block (IO ports 0xafe0-0xafe3, byte access)
----------------------------------------------------

Generic ACPI GPE block. Bit 1 (GPE.1) used to notify PCI hotplug/eject
event to ACPI BIOS, via SCI interrupt.

PCI slot injection notification pending (IO port 0xae00-0xae03, 4-byte access)
------------------------------------------------------------------------------

Slot injection notification pending. One bit per slot.

Read by ACPI BIOS GPE.1 handler to notify OS of injection
events.  Read-only.

PCI slot removal notification (IO port 0xae04-0xae07, 4-byte access)
--------------------------------------------------------------------

Slot removal notification pending. One bit per slot.

Read by ACPI BIOS GPE.1 handler to notify OS of removal
events.  Read-only.

PCI device eject (IO port 0xae08-0xae0b, 4-byte access)
-------------------------------------------------------

Write: Used by ACPI BIOS _EJ0 method to request device removal.
One bit per slot.

Read: Hotplug features register.  Used by platform to identify features
available.  Current base feature set (no bits set):

- Read-only "up" register @0xae00, 4-byte access, bit per slot
- Read-only "down" register @0xae04, 4-byte access, bit per slot
- Read/write "eject" register @0xae08, 4-byte access,
  write: bit per slot eject, read: hotplug feature set
- Read-only hotplug capable register @0xae0c, 4-byte access, bit per slot

PCI removability status (IO port 0xae0c-0xae0f, 4-byte access)
--------------------------------------------------------------

Used by ACPI BIOS _RMV method to indicate removability status to OS. One
bit per slot.  Read-only.

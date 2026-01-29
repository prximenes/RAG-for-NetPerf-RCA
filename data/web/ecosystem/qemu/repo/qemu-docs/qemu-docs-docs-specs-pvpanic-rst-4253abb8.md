---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/specs/pvpanic.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.257169+00:00"
}
                    ---
                    # docs/specs/pvpanic.rst

                    PVPANIC DEVICE
==============

pvpanic device is a simulated device, through which a guest panic
event is sent to qemu, and a QMP event is generated. This allows
management apps (e.g. libvirt) to be notified and respond to the event.

The management app has the option of waiting for GUEST_PANICKED events,
and/or polling for guest-panicked RunState, to learn when the pvpanic
device has fired a panic event.

The pvpanic device can be implemented as an ISA device (using IOPORT) or as a
PCI device.

ISA Interface
-------------

pvpanic exposes a single I/O port, by default 0x505. On read, the bits
recognized by the device are set. Software should ignore bits it doesn't
recognize. On write, the bits not recognized by the device are ignored.
Software should set only bits both itself and the device recognize.

Bit Definition
~~~~~~~~~~~~~~

bit 0
  a guest panic has happened and should be processed by the host
bit 1
  a guest panic has happened and will be handled by the guest;
  the host should record it or report it, but should not affect
  the execution of the guest.
bit 2
  a regular guest shutdown has happened and should be processed by the host

PCI Interface
-------------

The PCI interface is similar to the ISA interface except that it uses an MMIO
address space provided by its BAR0, 1 byte long. Any machine with a PCI bus
can enable a pvpanic device by adding ``-device pvpanic-pci`` to the command
line.

ACPI Interface
--------------

pvpanic device is defined with ACPI ID "QEMU0001". Custom methods:

RDPT
~~~~

To determine whether guest panic notification is supported.

Arguments
  None
Return
  Returns a byte, with the same semantics as the I/O port interface.

WRPT
~~~~

To send a guest panic event.

Arguments
  Arg0 is a byte to be written, with the same semantics as the I/O interface.
Return
  None

The ACPI device will automatically refer to the right port in case it
is modified.

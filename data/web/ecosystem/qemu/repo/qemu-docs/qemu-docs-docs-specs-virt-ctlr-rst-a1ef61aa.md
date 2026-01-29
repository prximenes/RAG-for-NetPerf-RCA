---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/specs/virt-ctlr.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.263293+00:00"
}
                    ---
                    # docs/specs/virt-ctlr.rst

                    Virtual System Controller
=========================

The ``virt-ctrl`` device is a simple interface defined for the pure
virtual machine with no hardware reference implementation to allow the
guest kernel to send command to the host hypervisor.

The specification can evolve, the current state is defined as below.

This is a MMIO mapped device using 256 bytes.

Two 32bit registers are defined:

the features register (read-only, address 0x00)
   This register allows the device to report features supported by the
   controller.
   The only feature supported for the moment is power control (0x01).

the command register (write-only, address 0x04)
   This register allows the kernel to send the commands to the hypervisor.
   The implemented commands are part of the power control feature and
   are reset (1), halt (2) and panic (3).
   A basic command, no-op (0), is always present and can be used to test the
   register access. This command has no effect.

---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/spice-port-fqdn.txt",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.220715+00:00"
}
                    ---
                    # docs/spice-port-fqdn.txt

                    A Spice port channel is an arbitrary communication between the Spice
server host side and the client side.

Thanks to the associated reverse fully qualified domain name (fqdn),
a Spice client can handle the various ports appropriately.

The following fqdn names are reserved by the QEMU project:

org.qemu.monitor.hmp.0
  QEMU human monitor

org.qemu.monitor.qmp.0:
  QEMU control monitor

org.qemu.console.serial.0
  QEMU virtual serial port

org.qemu.console.debug.0
  QEMU debug console

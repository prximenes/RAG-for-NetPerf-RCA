---
                {
  "source": "web",
  "label": "qemu-virtio-index",
  "url": "https://www.qemu.org/docs/master/system/devices/virtio/index.html",
  "description": "Virtio device overview and references; supports virtio-net performance/drops scenarios",
  "license": "QEMU documentation (see site for license)",
  "collected_at": "2025-12-15T17:15:28.214971+00:00"
}
                ---
                # QEMU Virtio Devices (Index)

                VirtIO Devices — QEMU  documentation
            QEMU
Contents:
- About QEMU
- System Emulation
- Introduction
- Invocation
- Device Emulation
- Common Terms
- Emulated Devices
- VirtIO Devices
- CAN Bus Emulation Support
- CanoKey QEMU
- Chip Card Interface Device (CCID)
- Compute Express Link (CXL)
- eMMC Emulation
- igb
- Inter-VM Shared Memory Flat Device
- Inter-VM Shared Memory device
- Sparc32 keyboard
- Network emulation
- NVMe Emulation
- Universal Second Factor (U2F) USB Key Device
- USB emulation
- vfio-user
- Keys in the graphical frontends
- Keys in the character backend multiplexer
- QEMU Monitor
- Disk Images
- QEMU virtio-net standby (net_failover)
- Direct Linux Boot
- Generic Loader
- Guest Loader
- QEMU Barrier Client
- VNC security
- TLS setup for network services
- Providing secret data to QEMU
- Client authorization
- GDB usage
- Record/replay
- Managed start up options
- Managing device boot order with bootindex properties
- Virtual CPU hotplug
- Persistent reservation managers
- QEMU System Emulator Targets
- Security
- Multi-process QEMU
- Confidential Guest Support
- Independent Guest Virtual Machine (IGVM) support
- QEMU VM templating
- Composable SR-IOV device
- User Mode Emulation
- Tools
- System Emulation Management and Interoperability
- System Emulation Guest Hardware Specifications
- Developer Information
- Glossary
QEMU
-
- System Emulation
- Device Emulation
- VirtIO Devices
- View page source
VirtIO Devices
VirtIO devices are paravirtualized devices designed to be efficient to
emulate and virtualize. Unless you are specifically trying to exercise
a driver for some particular hardware they are the recommended device
models to use for virtual machines.
The VirtIO specification is an open standard managed by OASIS. It
describes how a driver in a guest operating system interacts with
the device model provided by QEMU. Multiple Operating Systems
support drivers for VirtIO with Linux perhaps having the widest range
of device types supported.
The device implementation can either be provided wholly by QEMU, or in
concert with the kernel (known as vhost). The device implementation
can also be off-loaded to an external process via vhost user.
- VirtIO GPU
- VirtIO Persistent Memory
- VirtIO Sound
- vhost-user back ends
- vhost-user daemons in contrib
 PreviousNext
© Copyright 2025, The QEMU Project Developers.
  Built with Sphinx using a
    theme
    provided by Read the Docs.
This documentation is for QEMU version 10.1.93.
QEMU and this manual are released under the
GNU General Public License, version 2.
      jQuery(function () {
          SphinxRtdTheme.Navigation.enable(true);
      });

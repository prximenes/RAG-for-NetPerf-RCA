---
                {
  "source": "web",
  "label": "qemu-net-emulation",
  "url": "https://www.qemu.org/docs/master/system/devices/net.html",
  "description": "NIC models/backends (tap, user, bridge), core networking options; supports KVM/QEMU network scenarios",
  "license": "QEMU documentation (see site for license)",
  "collected_at": "2025-12-15T17:15:27.609296+00:00"
}
                ---
                # QEMU Network Emulation

                Network emulation — QEMU  documentation
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
- Network emulation
- View page source
Network emulation
QEMU can simulate several network cards (e.g. PCI or ISA cards on the PC
target) and can connect them to a network backend on the host or an
emulated hub. The various host network backends can either be used to
connect the NIC of the guest to a real network (e.g. by using a TAP
devices or the non-privileged user mode network stack), or to other
guest instances running in another QEMU process (e.g. by using the
socket host network backend).
Using TAP network interfaces
This is the standard way to connect QEMU to a real network. QEMU adds a
virtual network device on your host (called
```
tapN
```
), and you can then
configure it as if it was a real ethernet card.
Linux host
A distribution will generally provide specific helper scripts when it
packages QEMU. By default these are found at
```
/etc/qemu-ifup
```
 and
```
/etc/qemu-ifdown
```
 and are called appropriately when QEMU wants to
change the network state.
If QEMU is being run as a non-privileged user you may need properly
configure
```
sudo
```
 so that network commands in the scripts can be
executed as root.
You must verify that your host kernel supports the TAP network
interfaces: the device
```
/dev/net/tun
```
 must be present.
See Invocation to have examples of command
lines using the TAP network interfaces.
Windows host
There is a virtual ethernet driver for Windows 2000/XP systems, called
TAP-Win32. But it is not included in standard QEMU for Windows, so you
will need to get it separately. It is part of OpenVPN package, so
download OpenVPN from : https://openvpn.net/.
Using the user mode network stack
By using the option
```
-netuser
```
 (default configuration if no
```
-net
```
option is specified), QEMU uses a completely user mode network stack
(you don’t need root privilege to use the virtual network). The virtual
network configuration is the following:
```
guest(10.0.2.15)<------>Firewall/DHCPserver<----->Internet|(10.0.2.2)|---->DNSserver(10.0.2.3)|---->SMBserver(10.0.2.4)
```
The QEMU VM behaves as if it was behind a firewall which blocks all
incoming connections. You can use a DHCP client to automatically
configure the network in the QEMU VM. The DHCP server assign addresses
to the hosts starting from 10.0.2.15.
In order to check that the user mode network is working, you can ping
the address 10.0.2.2 and verify that you got an address in the range
10.0.2.x from the QEMU virtual DHCP server.
Note that ICMP traffic in general does not work with user mode
networking.
```
ping
```
, aka. ICMP echo, to the local router (10.0.2.2)
shall work, however. If you’re using QEMU on Linux >= 3.0, it can use
unprivileged ICMP ping sockets to allow
```
ping
```
 to the Internet. The
host admin has to set the ping_group_range in order to grant access to
those sockets. To allow ping for GID 100 (usually users group):
```
echo100100>/proc/sys/net/ipv4/ping_group_range
```
When using the built-in TFTP server, the router is also the TFTP server.
When using the
```
'-netdevuser,hostfwd=...'
```
 option, TCP, UDP or UNIX
connections can be redirected from the host to the guest. It allows for
example to redirect X11, telnet or SSH connections.
Using passt as the user mode network stack
passt can be used as a simple replacement for SLIRP (
```
-netuser
```
).
passt doesn’t require any capability or privilege. passt has
better performance than
```
-netuser
```
, full IPv6 support and better security
as it’s a daemon that is not executed in QEMU context.
passt can be used in the same way as the user backend (using
```
-netpasst
```
,
```
-netdevpasst
```
 or
```
-nicpasst
```
) or it can be launched manually and
connected to QEMU either by using a socket (
```
-netdevstream
```
) or by using
the vhost-user interface (
```
-netdevvhost-user
```
).
Using
```
-netdevstream
```
 or
```
-netdevvhost-user
```
 will allow the user to
enable functionalities not available through the passt backend interface
(like migration).
See passt(1) for more details on passt.
To use the passt backend interface
There is no need to start the daemon as QEMU will do it for you.
By default, passt will be started in the socket-based mode.
```
qemu-system-x86_64 [...OPTIONS...] -nic passt
(qemu) info network
e1000e.0: index=0,type=nic,model=e1000e,macaddr=52:54:00:12:34:56
 #net071: index=0,type=passt,stream,connected to pid 24846
```
```
qemu-system-x86_64 [...OPTIONS...] -net nic -net passt,tcp-ports=10001,udp-ports=10001
(qemu) info network
hub 0
 hub0port1: #net136: index=0,type=passt,stream,connected to pid 25204
 hub0port0: e1000e.0: index=0,type=nic,model=e1000e,macaddr=52:54:00:12:34:56
```
```
qemu-system-x86_64 [...OPTIONS...] -netdev passt,id=netdev0 -device virtio-net,mac=9a:2b:2c:2d:2e:2f,id=virtio0,netdev=netdev0
(qemu) info network
virtio0: index=0,type=nic,model=virtio-net-pci,macaddr=9a:2b:2c:2d:2e:2f
 netdev0: index=0,type=passt,stream,connected to pid 25428
```
To use the vhost-based interface, add the
```
vhost-user=on
```
 parameter and
select the virtio-net device:
```
qemu-system-x86_64 [...OPTIONS...] -nic passt,model=virtio,vhost-user=on
(qemu) info network
virtio-net-pci.0: index=0,type=nic,model=virtio-net-pci,macaddr=52:54:00:12:34:56
 #net006: index=0,type=passt,vhost-user,connected to pid 25731
```
To use socket based passt interface:
Start passt as a daemon:
```
passt--socket~/passt.socket
```
If
```
--socket
```
 is not provided, passt will print the path of the UNIX domain socket QEMU can connect to (
```
/tmp/passt_1.socket
```
,
```
/tmp/passt_2.socket
```
,
…). Then you can connect your QEMU instance to passt:
```
qemu-system-x86_64 [...OPTIONS...] -device virtio-net-pci,netdev=netdev0 -netdev stream,id=netdev0,server=off,addr.type=unix,addr.path=~/passt.socket
```
Where
```
~/passt.socket
```
 is the UNIX socket created by passt to
communicate with QEMU.
To use vhost-based interface:
Start passt with
```
--vhost-user
```
:
```
passt--vhost-user--socket~/passt.socket
```
Then to connect QEMU:
```
qemu-system-x86_64 [...OPTIONS...] -m $RAMSIZE -chardev socket,id=chr0,path=~/passt.socket -netdev vhost-user,id=netdev0,chardev=chr0 -device virtio-net,netdev=netdev0 -object memory-backend-memfd,id=memfd0,share=on,size=$RAMSIZE -numa node,memdev=memfd0
```
Where
```
$RAMSIZE
```
 is the memory size of your VM
```
-m
```
 and
```
-objectmemory-backend-memfd,size=
```
 must match.
Migration of passt:
When passt is connected to QEMU using the vhost-user interface it can
be migrated with QEMU and the network connections are not interrupted.
As passt runs with no privileges, it relies on passt-repair to save and
load the TCP connections state, using the TCP_REPAIR socket option.
The passt-repair helper needs to have the CAP_NET_ADMIN capability, or run as root. If passt-repair is not available, TCP connections will not be preserved.
Example of migration of a guest on the same host
Before being able to run passt-repair, the CAP_NET_ADMIN capability must be set
on the file, run as root:
```
setcapcap_net_admin+eip./passt-repair
```
Start passt for the source side:
```
passt--vhost-user--socket~/passt_src.socket--repair-path~/passt-repair_src.socket
```
Where
```
~/passt-repair_src.socket
```
 is the UNIX socket created by passt to
communicate with passt-repair. The default value is the
```
--socket
```
 path
appended with
```
.repair
```
.
Start passt-repair:
```
passt-repair~/passt-repair_src.socket
```
Start source side QEMU with a monitor to be able to send the migrate command:
```
qemu-system-x86_64 [...OPTIONS...] [...VHOST USER OPTIONS...] -monitor stdio
```
Start passt for the destination side:
```
passt--vhost-user--socket~/passt_dst.socket--repair-path~/passt-repair_dst.socket
```
Start passt-repair:
```
passt-repair~/passt-repair_dst.socket
```
Start QEMU with the
```
-incoming
```
 parameter:
```
qemu-system-x86_64 [...OPTIONS...] [...VHOST USER OPTIONS...] -incoming tcp:localhost:4444
```
Then in the source guest monitor the migration can be started:
```
(qemu)migratetcp:localhost:4444
```
A separate passt-repair instance must be started for every migration. In the case of a failed migration, passt-repair also needs to be restarted before trying
again.
Hubs
QEMU can simulate several hubs. A hub can be thought of as a virtual
connection between several network devices. These devices can be for
example QEMU virtual ethernet cards or virtual Host ethernet devices
(TAP devices). You can connect guest NICs or host network backends to
such a hub using the
```
-netdevhubport
```
 or
```
-nichubport
```
 options. The legacy
```
-net
```
 option also
connects the given device to the emulated hub with ID 0 (i.e. the
default hub) unless you specify a netdev with
```
-netnic,netdev=xxx
```
here.
Connecting emulated networks between QEMU instances
Using the
```
-netdevsocket
```
 (or
```
-nicsocket
```
 or
```
-netsocket
```
)
option, it is possible to create emulated networks that span several
QEMU instances. See the description of the
```
-netdevsocket
```
 option in
Invocation to have a basic
example.
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

---
                {
  "source": "web",
  "label": "kernel-docs-networking-index",
  "url": "https://docs.kernel.org/networking/",
  "description": "Kernel networking docs section (canonical docs site)",
  "license": null,
  "collected_at": "2025-12-15T17:15:25.751741+00:00"
}
                ---
                # Linux Kernel documentation (docs.kernel.org) — Networking

                Networking — The Linux Kernel  documentation
The Linux Kernel
6.19.0-rc1
Quick search
document.getElementById('searchbox').style.display = "block"Contents
- Development process
- Submitting patches
- Code of conduct
- Maintainer handbook
- All development-process docs
- Core API
- Driver APIs
- Subsystems
- Core subsystems
- Human interfaces
- Networking interfaces
- Networking
- NetLabel
- InfiniBand
- ISDN
- MHI
- Storage interfaces
- Other subsystems
- Locking
- Licensing rules
- Writing documentation
- Development tools
- Testing guide
- Hacking guide
- Tracing
- Fault injection
- Livepatching
- Rust
- Administration
- Build system
- Reporting issues
- Userspace tools
- Userspace API
- Firmware
- Firmware and Devicetree
- CPU architectures
- Unsorted documentation
- Translations
 <!--
  var sbar = document.getElementsByClassName("sphinxsidebar")[0];
  let currents = document.getElementsByClassName("current")
  if (currents.length) {
    sbar.scrollTop = currents[currents.length - 1].offsetTop;
  }
  --> This Page
- Show Source
English
- Chinese (Simplified)
Networking¶
Refer to Networking subsystem (netdev) for a guide on netdev development process specifics.
Contents:
- AF_XDP
- Overview
- Concepts
- Libbpf
- XSKMAP / BPF_MAP_TYPE_XSKMAP
- Configuration Flags and Socket Options
- Multi-Buffer Support
- Sample application
- FAQ
- Credits
- Bare UDP Tunnelling Module Documentation
- Special Handling
- Usage
- batman-adv
- Configuration
- Usage
- Logging/Debugging
- batctl
- Contact
- SocketCAN - Controller Area Network
- Overview / What is SocketCAN
- Motivation / Why Using the Socket API
- SocketCAN Concept
- How to use SocketCAN
- SocketCAN Core Module
- CAN Network Drivers
- SocketCAN Resources
- Credits
- The UCAN Protocol
- USB Endpoints
- CONTROL Messages
- IN Message Format
- OUT Message Format
- CAN Error Handling
- Example Conversation
- Hardware Device Drivers
- Asynchronous Transfer Mode (ATM) Device Drivers
- Controller Area Network (CAN) Device Drivers
- Cellular Modem Device Drivers
- Ethernet Device Drivers
- Fiber Distributed Data Interface (FDDI) Device Drivers
- Amateur Radio Device Drivers
- Wi-Fi Device Drivers
- WWAN Device Drivers
- Networking Diagnostics
- Diagnostic Concept for Investigating Twisted Pair Ethernet Variants at OSI Layer 1
- Distributed Switch Architecture
- Architecture
- Broadcom RoboSwitch Ethernet switch driver
- Broadcom Starfighter 2 Ethernet switch driver
- LAN9303 Ethernet switch driver
- NXP SJA1105 switch driver
- DSA switch configuration from userspace
- Linux Devlink Documentation
- Locking
- Nested instances
- Interface documentation
- Driver-specific documentation
- CAIF
- Linux CAIF
- Using Linux CAIF
- Netlink interface for ethtool
- Basic information
- Conventions
- Request header
- Bit sets
- List of message types
- STRSET_GET
- LINKINFO_GET
- LINKINFO_SET
- LINKMODES_GET
- LINKMODES_SET
- LINKSTATE_GET
- DEBUG_GET
- DEBUG_SET
- WOL_GET
- WOL_SET
- FEATURES_GET
- FEATURES_SET
- PRIVFLAGS_GET
- PRIVFLAGS_SET
- RINGS_GET
- RINGS_SET
- CHANNELS_GET
- CHANNELS_SET
- COALESCE_GET
- COALESCE_SET
- PAUSE_GET
- PAUSE_SET
- EEE_GET
- EEE_SET
- TSINFO_GET
- CABLE_TEST
- CABLE_TEST TDR
- TUNNEL_INFO
- FEC_GET
- FEC_SET
- MODULE_EEPROM_GET
- STATS_GET
- PHC_VCLOCKS_GET
- MODULE_GET
- MODULE_SET
- PSE_GET
- PSE_SET
- PSE_NTF
- RSS_GET
- RSS_SET
- RSS_CREATE_ACT
- RSS_DELETE_ACT
- PLCA_GET_CFG
- PLCA_SET_CFG
- PLCA_GET_STATUS
- MM_GET
- MM_SET
- MODULE_FW_FLASH_ACT
- PHY_GET
- TSCONFIG_GET
- TSCONFIG_SET
- MSE_GET
- Request translation
- IEEE 802.15.4 Developer’s Guide
- Introduction
- Socket API
- 6LoWPAN Linux implementation
- Drivers
- Device drivers API
- ISO 15765-2 (ISO-TP)
- Overview
- How to Use ISO-TP
- Examples
- J1939 Documentation
- Overview / What Is J1939
- Motivation
- J1939 concepts
- How to Use J1939
- Linux Networking and Network Devices APIs
- Linux Networking
- Network device support
- MSG_ZEROCOPY
- Intro
- Interface
- Implementation
- Testing
- FAILOVER
- Overview
- Net DIM - Generic Network Dynamic Interrupt Moderation
- Assumptions
- Introduction
- Net DIM Algorithm
- Registering a Network Device to DIM
- Example
- Tuning DIM
- Dynamic Interrupt Moderation (DIM) library API
- NET_FAILOVER
- Overview
- virtio-net accelerated datapath: STANDBY mode
- Live Migration of a VM with SR-IOV VF & virtio-net in STANDBY mode
- Page Pool API
- Architecture overview
- Monitoring
- API interface
- Coding examples
- PHY Abstraction Layer
- Purpose
- The MDIO bus
- (RG)MII/electrical interface considerations
- Connecting to a PHY
- Letting the PHY Abstraction Layer do Everything
- PHY interface modes
- Pause frames / flow control
- Keeping Close Tabs on the PAL
- Doing it all yourself
- PHY Device Drivers
- Board Fixups
- Standards
- phylink
- Overview
- Modes of operation
- Rough guide to converting a network driver to sfp/phylink
- IP-Aliasing
- Alias creation
- Alias deletion
- Alias (re-)configuring
- Relationship with main device
- Ethernet Bridging
- Introduction
- Bridge kAPI
- Bridge uAPI
- STP
- VLAN
- Multicast
- Switchdev
- Netfilter
- Other Features
- FAQ
- Contact Info
- External Links
- SNMP counter
- General IPv4 counters
- ICMP counters
- General TCP counters
- TCP Fast Open
- TCP Fast Path
- TCP abort
- TCP Hybrid Slow Start
- TCP retransmission and congestion control
- DSACK
- invalid SACK and DSACK
- SACK shift
- TCP out of order
- TCP PAWS
- TCP ACK skip
- TCP receive window
- Delayed ACK
- Tail Loss Probe (TLP)
- TCP Fast Open description
- SYN cookies
- Challenge ACK
- prune
- examples
- Checksum Offloads
- Introduction
- TX Checksum Offload
- LCO: Local Checksum Offload
- RCO: Remote Checksum Offload
- Segmentation Offloads
- Introduction
- TCP Segmentation Offload
- UDP Fragmentation Offload
- IPIP, SIT, GRE, UDP Tunnel, and Remote Checksum Offloads
- Generic Segmentation Offload
- Generic Receive Offload
- Partial Generic Segmentation Offload
- SCTP acceleration with GSO
- Scaling in the Linux Networking Stack
- Introduction
- RSS: Receive Side Scaling
- RPS: Receive Packet Steering
- RFS: Receive Flow Steering
- Accelerated RFS
- XPS: Transmit Packet Steering
- Per TX Queue rate limitation
- Further Information
- Kernel TLS
- Overview
- User interface
- Statistics
- Kernel TLS offload
- Kernel TLS operation
- Device configuration
- Normal operation
- Resync handling
- Error handling
- Performance metrics
- Statistics
- Notable corner cases, exceptions and additional requirements
- In-Kernel TLS Handshake
- Overview
- User handshake agent
- Kernel Handshake API
- Handshake Completion
- Linux NFC subsystem
- Architecture overview
- Device Driver Interface
- Userspace interface
- Netdev private dataroom for 6lowpan interfaces
- 6pack Protocol
- 1. What is 6pack, and what are the advantages to KISS?
- 2. Who has developed the 6pack protocol?
- 3. Where can I get the latest version of 6pack for LinuX?
- 4. Preparing the TNC for 6pack operation
- 5. Building and installing the 6pack driver
- 6. Known problems
- ARCnet Hardware
- Introduction to ARCnet
- Cabling ARCnet Networks
- Setting the Jumpers
- Unclassified Stuff
- Standard Microsystems Corp (SMC)
- Possibly SMC
- PureData Corp
- CNet Technology Inc. (8-bit cards)
- CNet Technology Inc. (16-bit cards)
- Lantech
- Acer
- Datapoint?
- Topware
- Thomas-Conrad
- Waterloo Microsystems Inc. ??
- No Name
- Tiara
- Other Cards
- ARCnet
- Where do I discuss these drivers?
- Other Drivers and Info
- Installing the Driver
- Loadable Module Support
- Using the Driver
- Multiple Cards in One Computer
- How do I get it to work with...?
- Using Multiprotocol ARCnet
- It works: what now?
- It doesn’t work: what now?
- I want to send money: what now?
- ATM
- AX.25
- Linux Ethernet Bonding Driver HOWTO
- Introduction
- 1. Bonding Driver Installation
- 2. Bonding Driver Options
- 3. Configuring Bonding Devices
- 4 Querying Bonding Configuration
- 5. Switch Configuration
- 6. 802.1q VLAN Support
- 7. Link Monitoring
- 8. Potential Sources of Trouble
- 9. SNMP agents
- 10. Promiscuous mode
- 11. Configuring Bonding for High Availability
- 12. Configuring Bonding for Maximum Throughput
- 13. Switch Behavior Issues
- 14. Hardware Specific Considerations
- 15. Frequently Asked Questions
- 16. Resources and Links
- cdc_mbim - Driver for CDC MBIM Mobile Broadband modems
- Command Line Parameters
- Basic usage
- MBIM control channel userspace ABI
- MBIM data channel userspace ABI
- References
- DCTCP (DataCenter TCP)
- Device Memory TCP
- Intro
- RX Interface
- TX Interface
- Implementation & Caveats
- Testing
- DNS Resolver Module
- Overview
- Compilation
- Setting up
- Usage
- Reading DNS Keys from Userspace
- Mechanism
- Debugging
- Softnet Driver Issues
- Probing guidelines
- Close/stop guidelines
- Transmit path guidelines
- EQL Driver: Serial IP Load Balancing HOWTO
- 1. Introduction
- 2. Kernel Configuration
- 3. Network Configuration
- 4. About the Slave Scheduler Algorithm
- 5. Testers’ Reports
- LC-trie implementation notes
- Node types
- A few concepts explained
- Comments
- Locking
- Main lookup mechanism
- Linux Socket Filtering aka Berkeley Packet Filter (BPF)
- Notice
- Introduction
- Structure
- Example
- BPF engine and instruction set
- JIT compiler
- BPF kernel internals
- Testing
- Misc
- Written by
- Generic HDLC layer
- Board-specific issues
- Generic Netlink
- Netlink Family Specifications
- Family
```
binder
```
 netlink specification
- Family
```
conntrack
```
 netlink specification
- Family
```
devlink
```
 netlink specification
- Family
```
dpll
```
 netlink specification
- Family
```
em
```
 netlink specification
- Family
```
ethtool
```
 netlink specification
- Family
```
fou
```
 netlink specification
- Family
```
handshake
```
 netlink specification
- Family
```
lockd
```
 netlink specification
- Family
```
mptcp_pm
```
 netlink specification
- Family
```
net-shaper
```
 netlink specification
- Family
```
netdev
```
 netlink specification
- Family
```
nfsd
```
 netlink specification
- Family
```
nftables
```
 netlink specification
- Family
```
nl80211
```
 netlink specification
- Family
```
nlctrl
```
 netlink specification
- Family
```
ovpn
```
 netlink specification
- Family
```
ovs_datapath
```
 netlink specification
- Family
```
ovs_flow
```
 netlink specification
- Family
```
ovs_vport
```
 netlink specification
- Family
```
psp
```
 netlink specification
- Family
```
rt-addr
```
 netlink specification
- Family
```
rt-link
```
 netlink specification
- Family
```
rt-neigh
```
 netlink specification
- Family
```
rt-route
```
 netlink specification
- Family
```
rt-rule
```
 netlink specification
- Family
```
tc
```
 netlink specification
- Family
```
tcp_metrics
```
 netlink specification
- Family
```
team
```
 netlink specification
- Family
```
wireguard
```
 netlink specification
- Generic networking statistics for netlink users
- Collecting:
- Export to userspace (Dump):
- TCA_STATS/TCA_XSTATS backward compatibility:
- Locking:
- Rate Estimator:
- Authors:
- The Linux kernel GTP tunneling module
- What is GTP
- The Linux GTP tunnelling module
- Userspace Programs with Linux Kernel GTP-U support
- Userspace Library / Command Line Utilities
- Protocol Versions
- IPv6
- Mailing List
- Issue Tracker
- History / Acknowledgements
- Architectural Details
- APN vs. Network Device
- Identifier Locator Addressing (ILA)
- Introduction
- ILA terminology
- Operation
- Transport checksum handling
- Identifier types
- Identifier formats
- Configuration
- Some examples
- IOAM6 Sysfs variables
- /proc/sys/net/conf/<iface>/ioam6_* variables:
- io_uring zero copy Rx
- Introduction
- NIC HW Requirements
- Usage
- Testing
- IP dynamic address hack-port v0.03
- IPsec
- IP Sysctl
- /proc/sys/net/ipv4/* Variables
- INET peer storage
- TCP variables
- UDP variables
- RAW variables
- CIPSOv4 Variables
- IP Variables
- /proc/sys/net/ipv6/* Variables
-
```
icmp/*
```
:
- /proc/sys/net/bridge/* Variables:
-
```
proc/sys/net/sctp/*
```
 Variables:
-
```
/proc/sys/net/core/*
```
-
```
/proc/sys/net/unix/*
```
- IPv6
- IPVLAN Driver HOWTO
- 1. Introduction:
- 2. Building and Installation:
- 3. Configuration:
- 4. Operating modes:
- 5. Mode flags:
- 6. What to choose (macvlan vs. ipvlan)?
- 6. Example configuration:
- IPvs-sysctl
- /proc/sys/net/ipv4/vs/* Variables:
- Kernel Connection Multiplexor
- KCM sockets
- Multiplexor
- TCP sockets & Psocks
- Connected mode semantics
- Socket types
- User interface
- Use in applications
- L2TP
- Overview
- L2TP APIs
- Internal Implementation
- Miscellaneous
- The Linux LAPB Module Interface
- Structures
- LAPB Initialisation Structure
- LAPB Parameter Structure
- Functions
- Callbacks
- How to use packet injection with mac80211
- Management Component Transport Protocol (MCTP)
- Structure: interfaces & networks
- Sockets API
- Kernel internals
- MPLS Sysfs variables
- /proc/sys/net/mpls/* Variables:
- Multipath TCP (MPTCP)
- Introduction
- Use cases
- Concepts
- Sockets API
- Design choices
- MPTCP Sysfs variables
- /proc/sys/net/mptcp/* Variables
- HOWTO for multiqueue network device support
- Section 1: Base driver requirements for implementing multiqueue support
- Section 2: Qdisc support for multiqueue devices
- Section 3: Brief howto using MULTIQ for multiqueue devices
- Multi-PF Netdev
- Contents
- Background
- Overview
- mlx5 implementation
- Channels distribution
- Observability
- Steering
- Mutually exclusive features
- NAPI
- Driver API
- User API
- Common Networking Struct Cachelines
- inet_connection_sock struct fast path usage breakdown
- inet_sock struct fast path usage breakdown
- net_device struct fast path usage breakdown
- netns_ipv4 struct fast path usage breakdown
- netns_ipv4 enum fast path usage breakdown
- tcp_sock struct fast path usage breakdown
- Netconsole
- Introduction:
- Sender and receiver configuration:
- Dynamic reconfiguration:
- Extended console:
- Miscellaneous notes:
- Netdev features mess and how to get out from it alive
- Part I: Feature sets
- Part II: Controlling enabled features
- Part III: Implementation hints
- Part IV: Features
- Network Devices, the Kernel, and You!
- Introduction
- struct net_device lifetime rules
- MTU
- struct net_device synchronization rules
- struct napi_struct synchronization rules
- netdev instance lock
- NETDEV_INTERNAL symbol namespace
- Netfilter Sysfs variables
- /proc/sys/net/netfilter/* Variables:
- NETIF Msg Level
- History
- Netmem Support for Network Drivers
- Driver RX Requirements
- Driver TX Requirements
- Resilient Next-hop Groups
- Algorithm
- Offloading & Driver Feedback
- Netlink UAPI
- Usage
- Netdevsim
- Netfilter Conntrack Sysfs variables
- /proc/sys/net/netfilter/nf_conntrack_* Variables:
- Netfilter’s flowtable infrastructure
- Overview
- Example configuration
- Layer 2 encapsulation
- Bridge and IP forwarding
- Counters
- Hardware offload
- Limitations
- More reading
- OPEN Alliance 10BASE-T1x MAC-PHY Serial Interface (TC6) Framework Support
- Introduction
- Overview
- Protocol Overview
- Reference
- Hardware Architecture
- Software Architecture
- Implementation
- Open vSwitch datapath developer documentation
- Flow key compatibility
- Flow key format
- Wildcarded flow key format
- Unique flow identifiers
- Basic rule for evolving flow keys
- Handling malformed packets
- Other rules
- Operational States
- 1. Introduction
- 2. Querying from userspace
- 3. Kernel driver API
- 4. Setting from userspace
- Packet MMAP
- Abstract
- Why use PACKET_MMAP
- How to use mmap() to improve capture process
- How to use mmap() directly to improve capture process
- How to use mmap() directly to improve transmission process
- PACKET_MMAP settings
- PACKET_MMAP setting constraints
- PACKET_MMAP buffer size calculator
- What TPACKET versions are available and when to use them?
- AF_PACKET fanout mode
- AF_PACKET TPACKET_V3 example
- PACKET_QDISC_BYPASS
- PACKET_TIMESTAMP
- Miscellaneous bits
- THANKS
- Linux Phonet protocol family
- Introduction
- Packets format
- Link layer
- Network layer
- Low-level datagram protocol
- Resource subscription
- Phonet Pipe protocol
- Authors
- PHY link topology
- Overview
- API
- UAPI
- HOWTO for the linux packet generator
- Tuning NIC for max performance
- Kernel threads
- Viewing devices
- Configuring devices
- Sample scripts
- Interrupt affinity
- Enable IPsec
- Disable shared SKB
- Current commands and configuration options
- PLIP: The Parallel Line Internet Protocol Device
- PLIP Introduction
- PLIP driver details
- PLIP hardware interconnection
- PPP Generic Driver and Channel Interface
- PPP channel API
- Buffering and flow control
- SMP safety
- Interface to pppd
- The proc/net/tcp and proc/net/tcp6 variables
- Power Sourcing Equipment (PSE) Documentation
- Power Sourcing Equipment (PSE) in IEEE 802.3 Standard
- PSE Power Interface (PSE PI) Documentation
- PSP Security Protocol
- Protocol
- User facing API
- Kernel implementation
- How to use radiotap headers
- Pointer to the radiotap include file
- Structure of the header
- Requirements for arguments
- Example valid radiotap header
- Using the Radiotap Parser
- RDS
- Overview
- RDS Architecture
- Socket Interface
- RDMA for RDS
- Congestion Notifications
- RDS Protocol
- RDS Transport Layer
- RDS Kernel Structures
- Connection management
- The send path
- The recv path
- Multipath RDS (mprds)
- Linux wireless regulatory documentation
- Keeping regulatory domains in userspace
- How to get regulatory domains to the kernel
- How to get regulatory domains to the kernel (old CRDA solution)
- Who asks for regulatory domains?
- Example code - drivers hinting an alpha2:
- Example code - drivers providing a built in regulatory domain:
- Statically compiled regulatory database
- Network Function Representors
- Motivation
- Definitions
- What does a representor do?
- What functions should have a representor?
- How are representors created?
- How are representors identified?
- How do representors interact with TC rules?
- Configuring the representee’s MAC
- RxRPC Network Protocol
- Overview
- RxRPC Protocol Summary
- AF_RXRPC Driver Model
- Control Messages
- Socket Options
- Security
- Example Client Usage
- Example Server Usage
- AF_RXRPC Kernel Interface
- Configurable Parameters
- API Function Reference
- Linux Kernel SCTP
- Caveats
- LSM/SeLinux secid
- Seg6 Sysfs variables
- /proc/sys/net/conf/<iface>/seg6_* variables:
- /proc/sys/net/ipv6/seg6_* variables:
- struct sk_buff
- Basic sk_buff geometry
- Shared skbs and skb clones
- dataref and headerless skbs
- Checksum information
- SMC Sysctl
- /proc/sys/net/smc/* Variables
- NIC SR-IOV APIs
- Legacy API
- Interface statistics
- Overview
- uAPIs
- struct rtnl_link_stats64
- Notes for driver authors
- Stream Parser (strparser)
- Introduction
- Interface
- Functions
- Callbacks
- Statistics
- Message assembly limits
- Author
- Ethernet switch device driver model (switchdev)
- Include Files
- Configuration
- Switch Ports
- L2 Forwarding Offload
- L3 Routing Offload
- Device driver expected behavior
- Sysfs tagging
- TC Actions - Environmental Rules
- TC queue based filtering
- TCP Authentication Option Linux implementation (RFC5925)
- 1. Introduction
- 2. In-kernel MKTs database vs database in userspace
- 3. uAPI
- 4.
```
setsockopt()
```
 vs
```
accept()
```
 race
- 5. Interaction with TCP-MD5
- 6. SNE Linux implementation
- 7. Links
- Thin-streams and TCP
- References
- Team
- Timestamping
- 1. Control Interfaces
- 2 Data Interfaces
- 3. Hardware Timestamping configuration: ETHTOOL_MSG_TSCONFIG_SET/GET
- Linux Kernel TIPC
- Introduction
- Implementation
- Transparent proxy support
- 1. Making non-local sockets work
- 2. Redirecting traffic
- 3. Iptables and nf_tables extensions
- 4. Application support
- Universal TUN/TAP device driver
- 1. Description
- 2. Configuration
- 3. Program interface
- Universal TUN/TAP device driver Frequently Asked Question
- The UDP-Lite protocol (RFC 3828)
- 1. Applications
- 2. Programming API
- 3. Header Files
- 4. Kernel Behaviour with Regards to the Various Socket Options
- 5. UDP-Lite Runtime Statistics and their Meaning
- 6. IPtables
- 7. Maintainer Address
- Virtual Routing and Forwarding (VRF)
- The VRF Device
- Using iproute2 for VRFs
- Virtual eXtensible Local Area Networking documentation
- Linux X.25 Project
- X.25 Device Driver Interface
- Packet Layer to Device Driver
- Device Driver to Packet Layer
- Requirements for the device driver
- XFRM Framework
- XFRM device - offloading the IPsec computations
- XFRM proc - /proc/net/xfrm_* files
- XFRM sync
- XFRM Syscall
- XDP RX Metadata
- General Design
- AF_XDP
- XDP_PASS
- bpf_redirect_map
- bpf_tail_call
- Supported Devices
- Driver Implementation
- Example
- AF_XDP TX Metadata
- General Design
- Software TX Checksum
- Launch Time
- Querying Device Capabilities
- Example
      ©The kernel development community.
      |
      Powered by Sphinx 5.3.0
      & Alabaster 0.7.16
      |
      Page source

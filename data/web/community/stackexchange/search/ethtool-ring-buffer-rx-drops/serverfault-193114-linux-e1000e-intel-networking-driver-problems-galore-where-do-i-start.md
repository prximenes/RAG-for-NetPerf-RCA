---
            {
  "source": "stackexchange",
  "license": "CC BY-SA 4.0 (Stack Exchange)",
  "site": "serverfault",
  "question_id": 193114,
  "link": "https://serverfault.com/questions/193114/linux-e1000e-intel-networking-driver-problems-galore-where-do-i-start",
  "score": 26,
  "views": 78217,
  "answer_id": 219658,
  "answer_kind": "accepted",
  "tags": [
    "linux",
    "ubuntu",
    "linux-networking",
    "ubuntu-10.10"
  ],
  "query_label": "ethtool-ring-buffer-rx-drops",
  "description": "NIC ring buffer tuning / rx_dropped (scenario_06)",
  "collected_at": "2025-12-13T16:07:07.758600+00:00"
}
            ---
            # Linux e1000e (Intel networking driver) problems galore, where do I start?

            ## Question
            I'm currently having a major problem with
```
e1000e
```
 (not working at all) in Ubuntu Maverick (1.0.2-k4), after resume I'm getting a lot of stuff in dmesg:
```
```
[ 9085.820197] e1000e 0000:02:00.0: PCI INT A disabled
[ 9089.907756] e1000e: Intel(R) PRO/1000 Network Driver - 1.0.2-k4
[ 9089.907762] e1000e: Copyright (c) 1999 - 2009 Intel Corporation.
[ 9089.907797] e1000e 0000:02:00.0: Disabling ASPM  L1
[ 9089.907827] e1000e 0000:02:00.0: PCI INT A -> GSI 16 (level, low) -> IRQ 16
[ 9089.907857] e1000e 0000:02:00.0: setting latency timer to 64
[ 9089.908529] e1000e 0000:02:00.0: irq 44 for MSI/MSI-X
[ 9089.908922] e1000e 0000:02:00.0: Disabling ASPM L0s
[ 9089.908954] e1000e 0000:02:00.0: (unregistered net_device): PHY reset is blocked due to SOL/IDER session.
[ 9090.024625] e1000e 0000:02:00.0: eth0: (PCI Express:2.5GB/s:Width x1) 00:0a:e4:3e:ce:74
[ 9090.024630] e1000e 0000:02:00.0: eth0: Intel(R) PRO/1000 Network Connection
[ 9090.024712] e1000e 0000:02:00.0: eth0: MAC: 2, PHY: 2, PBA No: 005302-003
[ 9090.109492] e1000e 0000:02:00.0: irq 44 for MSI/MSI-X
[ 9090.164219] e1000e 0000:02:00.0: irq 44 for MSI/MSI-X
```
```
and, a bunch of
```
```
[ 2128.005447] e1000e 0000:02:00.0: eth0: Detected Hardware Unit Hang:
[ 2128.005452]   TDH                  <89>
[ 2128.005454]   TDT                  <27>
[ 2128.005456]   next_to_use          <27>
[ 2128.005458]   next_to_clean        <88>
[ 2128.005460] buffer_info[next_to_clean]:
[ 2128.005463]   time_stamp           <6e608>
[ 2128.005465]   next_to_watch        <8a>
[ 2128.005467]   jiffies              <6f929>
[ 2128.005469]   next_to_watch.status <0>
[ 2128.005471] MAC Status             <80080703>
[ 2128.005473] PHY Status             <796d>
[ 2128.005475] PHY 1000BASE-T Status  <4000>
[ 2128.005477] PHY Extended Status    <3000>
[ 2128.005480] PCI Status             <10>
```
```
I decided to compile the latest stable
```
e1000e
```
 to
```
1.2.17
```
, now I'm getting:
```
```
[ 9895.678050] e1000e: Intel(R) PRO/1000 Network Driver - 1.2.17-NAPI
[ 9895.678055] e1000e: Copyright(c) 1999 - 2010 Intel Corporation.
[ 9895.678098] e1000e 0000:02:00.0: Disabling ASPM  L1
[ 9895.678129] e1000e 0000:02:00.0: PCI INT A -> GSI 16 (level, low) -> IRQ 16
[ 9895.678162] e1000e 0000:02:00.0: setting latency timer to 64
[ 9895.679136] e1000e 0000:02:00.0: irq 44 for MSI/MSI-X
[ 9895.679160] e1000e 0000:02:00.0: Disabling ASPM L0s
[ 9895.679192] e1000e 0000:02:00.0: (unregistered net_device): PHY reset is blocked due to SOL/IDER session.
[ 9895.791758] e1000e 0000:02:00.0: eth0: (PCI Express:2.5GB/s:Width x1) 00:0a:e4:3e:ce:74
[ 9895.791766] e1000e 0000:02:00.0: eth0: Intel(R) PRO/1000 Network Connection
[ 9895.791850] e1000e 0000:02:00.0: eth0: MAC: 3, PHY: 2, PBA No: 005302-003
[ 9895.892464] e1000e 0000:02:00.0: irq 44 for MSI/MSI-X
[ 9895.948175] e1000e 0000:02:00.0: irq 44 for MSI/MSI-X
[ 9895.949111] ADDRCONF(NETDEV_UP): eth0: link is not ready
[ 9895.954694] e1000e: eth0 NIC Link is Up 10 Mbps Full Duplex, Flow Control: RX/TX
[ 9895.954703] e1000e 0000:02:00.0: eth0: 10/100 speed: disabling TSO
[ 9895.955157] ADDRCONF(NETDEV_CHANGE): eth0: link becomes ready
[ 9906.832056] eth0: no IPv6 routers present
```
```
With
```
1.2.20
```
 I get:
```
```
[ 9711.525465] e1000e: Intel(R) PRO/1000 Network Driver - 1.2.20-NAPI
[ 9711.525472] e1000e: Copyright(c) 1999 - 2010 Intel Corporation.
[ 9711.525521] e1000e 0000:02:00.0: Disabling ASPM  L1
[ 9711.525554] e1000e 0000:02:00.0: PCI INT A -> GSI 16 (level, low) -> IRQ 16
[ 9711.525586] e1000e 0000:02:00.0: setting latency timer to 64
[ 9711.526460] e1000e 0000:02:00.0: irq 45 for MSI/MSI-X
[ 9711.526487] e1000e 0000:02:00.0: Disabling ASPM L0s
[ 9711.526523] e1000e 0000:02:00.0: (unregistered net_device): PHY reset is blocked due to SOL/IDER session.
[ 9711.639763] e1000e 0000:02:00.0: eth0: (PCI Express:2.5GB/s:Width x1) 00:0a:e4:3e:ce:74
[ 9711.639771] e1000e 0000:02:00.0: eth0: Intel(R) PRO/1000 Network Connection
[ 9711.639854] e1000e 0000:02:00.0: eth0: MAC: 3, PHY: 2, PBA No: 005302-003
[ 9712.060770] e1000e 0000:02:00.0: irq 45 for MSI/MSI-X
[ 9712.116195] e1000e 0000:02:00.0: irq 45 for MSI/MSI-X
[ 9712.117098] ADDRCONF(NETDEV_UP): eth0: link is not ready
[ 9712.122684] e1000e: eth0 NIC Link is Up 100 Mbps Full Duplex, Flow Control: RX/TX
[ 9712.122693] e1000e 0000:02:00.0: eth0: 10/100 speed: disabling TSO
[ 9712.123142] ADDRCONF(NETDEV_CHANGE): eth0: link becomes ready
[ 9722.920014] eth0: no IPv6 routers present
```
```
But, I'm still getting these
```
```
[ 9982.992851] PCI Status             <10>
[ 9984.993602] e1000e 0000:02:00.0: eth0: Detected Hardware Unit Hang:
[ 9984.993606]   TDH                  <5d>
[ 9984.993608]   TDT                  <6b>
[ 9984.993611]   next_to_use          <6b>
[ 9984.993613]   next_to_clean        <5b>
[ 9984.993615] buffer_info[next_to_clean]:
[ 9984.993617]   time_stamp           <24da80>
[ 9984.993619]   next_to_watch        <5d>
[ 9984.993621]   jiffies              <24f200>
[ 9984.993624]   next_to_watch.status <0>
[ 9984.993626] MAC Status             <80080703>
[ 9984.993628] PHY Status             <796d>
[ 9984.993630] PHY 1000BASE-T Status  <4000>
[ 9984.993632] PHY Extended Status    <3000>
[ 9984.993635] PCI Status             <10>
[ 9986.001047] e1000e 0000:02:00.0: eth0: Reset adapter
[ 9986.176202] e1000e: eth0 NIC Link is Up 10 Mbps Full Duplex, Flow Control: RX/TX
[ 9986.176211] e1000e 0000:02:00.0: eth0: 10/100 speed: disabling TSO
```
```
I'm not sure where to start troubleshooting this. Any ideas?
Here is the result of
```
ethtool -d eth0
```
```
```
MAC Registers
-------------
0x00000: CTRL (Device control register)  0x18100248
      Endian mode (buffers):             little
      Link reset:                        reset
      Set link up:                       1
      Invert Loss-Of-Signal:             no
      Receive flow control:              enabled
      Transmit flow control:             enabled
      VLAN mode:                         disabled
      Auto speed detect:                 disabled
      Speed select:                      1000Mb/s
      Force speed:                       no
      Force duplex:                      no
0x00008: STATUS (Device status register) 0x80080703
      Duplex:                            full
      Link up:                           link config
      TBI mode:                          disabled
      Link speed:                        10Mb/s
      Bus type:                          PCI Express
      Port number:                       0
0x00100: RCTL (Receive control register) 0x04048002
      Receiver:                          enabled
      Store bad packets:                 disabled
      Unicast promiscuous:               disabled
      Multicast promiscuous:             disabled
      Long packet:                       disabled
      Descriptor minimum threshold size: 1/2
      Broadcast accept mode:             accept
      VLAN filter:                       enabled
      Canonical form indicator:          disabled
      Discard pause frames:              filtered
      Pass MAC control frames:           don't pass
      Receive buffer size:               2048
0x02808: RDLEN (Receive desc length)     0x00001000
0x02810: RDH   (Receive desc head)       0x00000001
0x02818: RDT   (Receive desc tail)       0x000000F0
0x02820: RDTR  (Receive delay timer)     0x00000000
0x00400: TCTL (Transmit ctrl register)   0x3103F0FA
      Transmitter:                       enabled
      Pad short packets:                 enabled
      Software XOFF Transmission:        disabled
      Re-transmit on late collision:     enabled
0x03808: TDLEN (Transmit desc length)    0x00001000
0x03810: TDH   (Transmit desc head)      0x00000000
0x03818: TDT   (Transmit desc tail)      0x00000000
0x03820: TIDV  (Transmit delay timer)    0x00000008
PHY type:                                IGP2
```
```
and
```
ethtool -c eth0
```
```
```
Coalesce parameters for eth0:
Adaptive RX: off  TX: off
stats-block-usecs: 0
sample-interval: 0
pkt-rate-low: 0
pkt-rate-high: 0
rx-usecs: 3
rx-frames: 0
rx-usecs-irq: 0
rx-frames-irq: 0
tx-usecs: 0
tx-frames: 0
tx-usecs-irq: 0
tx-frames-irq: 0
rx-usecs-low: 0
rx-frame-low: 0
tx-usecs-low: 0
tx-frame-low: 0
rx-usecs-high: 0
rx-frame-high: 0
tx-usecs-high: 0
tx-frame-high: 0
```
```
Here is also the
```
lspci -vvv
```
 for this controller
```
```
02:00.0 Ethernet controller: Intel Corporation 82573L Gigabit Ethernet Controller
    Subsystem: Lenovo ThinkPad X60s
    Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx+
    Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
    Latency: 0, Cache Line Size: 64 bytes
    Interrupt: pin A routed to IRQ 45
    Region 0: Memory at ee000000 (32-bit, non-prefetchable) [size=128K]
    Region 2: I/O ports at 2000 [size=32]
    Capabilities: [c8] Power Management version 2
        Flags: PMEClk- DSI+ D1- D2- AuxCurrent=0mA PME(D0+,D1-,D2-,D3hot+,D3cold+)
        Status: D0 NoSoftRst- PME-Enable- DSel=0 DScale=1 PME-
    Capabilities: [d0] MSI: Enable+ Count=1/1 Maskable- 64bit+
        Address: 00000000fee0300c  Data: 415a
    Capabilities: [e0] Express (v1) Endpoint, MSI 00
        DevCap: MaxPayload 256 bytes, PhantFunc 0, Latency L0s <512ns, L1 <64us
            ExtTag- AttnBtn- AttnInd- PwrInd- RBE- FLReset-
        DevCtl: Report errors: Correctable+ Non-Fatal+ Fatal+ Unsupported+
            RlxdOrd+ ExtTag- PhantFunc- AuxPwr- NoSnoop+
            MaxPayload 128 bytes, MaxReadReq 512 bytes
        DevSta: CorrErr- UncorrErr- FatalErr- UnsuppReq- AuxPwr+ TransPend-
        LnkCap: Port #0, Speed 2.5GT/s, Width x1, ASPM L0s L1, Latency L0 <128ns, L1 <64us
            ClockPM+ Surprise- LLActRep- BwNot-
        LnkCtl: ASPM Disabled; RCB 64 bytes Disabled- Retrain- CommClk+
            ExtSynch- ClockPM+ AutWidDis- BWInt- AutBWInt-
        LnkSta: Speed 2.5GT/s, Width x1, TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
    Capabilities: [100 v1] Advanced Error Reporting
        UESta:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq+ ACSViol-
        UEMsk:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
        UESvrt: DLP+ SDES- TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP+ ECRC- UnsupReq- ACSViol-
        CESta:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- NonFatalErr-
        CEMsk:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- NonFatalErr-
        AERCap: First Error Pointer: 14, GenCap- CGenEn- ChkCap- ChkEn-
    Capabilities: [140 v1] Device Serial Number 00-0a-e4-ff-ff-3e-ce-74
    Kernel driver in use: e1000e
    Kernel modules: e1000e
```
```
I filed a bug on this upstream, still no idea how to get more useful information.
Here is a the result of the running that script
EEPROM FIX UPDATE
```
```
$ sudo bash fixeep-82573-dspd.sh eth0
eth0: is a "82573L Gigabit Ethernet Controller"
This fixup is applicable to your hardware
Your eeprom is up to date, no changes were made
```
```
Do I still need to do anything? Also here is my EEPROM dump
```
```
$ sudo ethtool -e eth0
Offset      Values
------      ------
0x0000      00 0a e4 3e ce 74 30 0b b2 ff 51 00 ff ff ff ff
0x0010      53 00 03 02 6b 02 7e 20 aa 17 9a 10 86 80 df 80
0x0020      00 00 00 20 54 7e 00 00 14 00 da 00 04 00 00 27
0x0030      c9 6c 50 31 3e 07 0b 04 8b 29 00 00 00 f0 02 0f
0x0040      08 10 00 00 04 0f ff 7f 01 4d ff ff ff ff ff ff
0x0050      14 00 1d 00 14 00 1d 00 af aa 1e 00 00 00 1d 00
0x0060      00 01 00 40 1f 12 07 40 ff ff ff ff ff ff ff ff
0x0070      ff ff ff ff ff ff ff ff ff ff ff ff ff ff 4a e0
```
```
I'd also like to note that I used
```
eth0
```
 every day for years and until recently never had an issue.

            ## Accepted Answer
            Please try booting the kernel with the
```
pcie_aspm=off
```
 kernel parameter.

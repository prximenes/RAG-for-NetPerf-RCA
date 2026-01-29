---
            {
  "source": "stackexchange",
  "license": "CC BY-SA 4.0 (Stack Exchange)",
  "site": "serverfault",
  "question_id": 527440,
  "link": "https://serverfault.com/questions/527440/too-many-tcp-connections-causes-disconnections",
  "score": 6,
  "views": 36133,
  "answer_id": 527670,
  "tags": [
    "networking",
    "tcp",
    "centos5",
    "linux-networking"
  ],
  "query_label": "tcp-too-many-connections",
  "description": "Failures under many TCP connections; useful for conntrack exhaustion/limits reasoning",
  "collected_at": "2025-12-13T15:57:36.496313+00:00"
}
            ---
            # Too many TCP connections causes disconnections

            ## Question
            I have a game server which runs with TCP connections. Server disconnects users randomly. I think its related with TCP settings of server.
In local development environment written code can handle 8000+ concurrent users without any disconnection or error (at localhost).
But in real deployed Centos 5 64bit Server, server creating these disconnections independent from concurrent tcp connection amount.
Server seems to be not able to handle throughput.
```
```
netstat -s -t
IcmpMsg:
    InType0: 31
    InType3: 87717
    InType4: 699
    InType5: 2
    InType8: 1023781
    InType11: 7211
    OutType0: 1023781
    OutType3: 603
Tcp:
    8612766 active connections openings
    14255236 passive connection openings
    12174 failed connection attempts
    319225 connection resets received
    723 connections established
    6351090913 segments received
    6180297746 segments send out
    45791634 segments retransmited
    0 bad segments received.
    1664280 resets sent
TcpExt:
    46244 invalid SYN cookies received
    3745 resets received for embryonic SYN_RECV sockets
    327 ICMP packets dropped because they were out-of-window
    1 ICMP packets dropped because socket was locked
    11475281 TCP sockets finished time wait in fast timer
    140 time wait sockets recycled by time stamp
    1569 packets rejects in established connections because of timestamp
    103783714 delayed acks sent
    6929 delayed acks further delayed because of locked socket
    Quick ack mode was activated 6210096 times
    1806 times the listen queue of a socket overflowed
    1806 SYNs to LISTEN sockets ignored
    1080380601 packets directly queued to recvmsg prequeue.
    31441059 packets directly received from backlog
    5272599307 packets directly received from prequeue
    324498008 packets header predicted
    1143146 packets header predicted and directly queued to user
    3217838883 acknowledgments not containing data received
    1027969883 predicted acknowledgments
    395 times recovered from packet loss due to fast retransmit
    257420 times recovered from packet loss due to SACK data
    5843 bad SACKs received
    Detected reordering 29 times using FACK
    Detected reordering 12 times using SACK
    Detected reordering 1 times using reno fast retransmit
    Detected reordering 809 times using time stamp
    1602 congestion windows fully recovered
    1917 congestion windows partially recovered using Hoe heuristic
    TCPDSACKUndo: 8196226
    7850525 congestion windows recovered after partial ack
    139681 TCP data loss events
    TCPLostRetransmit: 26
    10139 timeouts after reno fast retransmit
    2802678 timeouts after SACK recovery
    86212 timeouts in loss state
    273698 fast retransmits
    19494 forward retransmits
    2637236 retransmits in slow start
    33381883 other TCP timeouts
    TCPRenoRecoveryFail: 92
    19488 sack retransmits failed
    7 times receiver scheduled too late for direct processing
    6354641 DSACKs sent for old packets
    333 DSACKs sent for out of order packets
    20615579 DSACKs received
    2724 DSACKs for out of order packets received
    123034 connections reset due to unexpected data
    91876 connections reset due to early user close
    169244 connections aborted due to timeout
    28736 times unabled to send RST due to no memory
IpExt:
    InMcastPkts: 2
```
```
What make me thinking is these seems to be very problematic.
```
```
123034 connections reset due to unexpected data
91876 connections reset due to early user close
28736 times unabled to send RST due to no memory
```
```
How can i fix these errors? Do i need to make TCP tuning?
edit: some sysctl info:
```
```
sysctl -A | grep net | grep mem
net.ipv4.udp_wmem_min = 4096
net.ipv4.udp_rmem_min = 4096
net.ipv4.udp_mem = 772704       1030272 1545408
net.ipv4.tcp_rmem = 4096        87380   4194304
net.ipv4.tcp_wmem = 4096        16384   4194304
net.ipv4.tcp_mem = 196608       262144  393216
net.ipv4.igmp_max_memberships = 20
net.core.optmem_max = 20480
net.core.rmem_default = 129024
net.core.wmem_default = 129024
net.core.rmem_max = 131071
net.core.wmem_max = 131071
```
```
edit: ethtool infos for 2 detected ethernet cards:
```
```
Settings for eth0:
        Supported ports: [ TP ]
        Supported link modes:   10baseT/Half 10baseT/Full
                                100baseT/Half 100baseT/Full
                                1000baseT/Full
        Supports auto-negotiation: Yes
        Advertised link modes:  10baseT/Half 10baseT/Full
                                100baseT/Half 100baseT/Full
                                1000baseT/Full
        Advertised auto-negotiation: Yes
        Speed: 1000Mb/s
        Duplex: Full
        Port: Twisted Pair
        PHYAD: 1
        Transceiver: internal
        Auto-negotiation: on
        Supports Wake-on: g
        Wake-on: d
        Link detected: yes
Settings for eth1:
        Supported ports: [ TP ]
        Supported link modes:   10baseT/Half 10baseT/Full
                                100baseT/Half 100baseT/Full
                                1000baseT/Full
        Supports auto-negotiation: Yes
        Advertised link modes:  10baseT/Half 10baseT/Full
                                100baseT/Half 100baseT/Full
                                1000baseT/Full
        Advertised auto-negotiation: Yes
        Speed: Unknown!
        Duplex: Half
        Port: Twisted Pair
        PHYAD: 1
        Transceiver: internal
        Auto-negotiation: on
        Supports Wake-on: g
        Wake-on: d
        Link detected: no
```
```

            ## Accepted Answer
            Do you increase the FD limit?
You can obtain some info here http://www.cyberciti.biz/faq/linux-increase-the-maximum-number-of-open-files/

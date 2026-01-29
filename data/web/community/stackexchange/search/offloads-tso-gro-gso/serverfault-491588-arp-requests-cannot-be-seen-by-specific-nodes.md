---
            {
  "source": "stackexchange",
  "license": "CC BY-SA 4.0 (Stack Exchange)",
  "site": "serverfault",
  "question_id": 491588,
  "link": "https://serverfault.com/questions/491588/arp-requests-cannot-be-seen-by-specific-nodes",
  "score": 12,
  "views": 6915,
  "answer_id": 520976,
  "answer_kind": "accepted",
  "tags": [
    "linux",
    "networking",
    "wifi",
    "linux-networking",
    "arp"
  ],
  "query_label": "offloads-tso-gro-gso",
  "description": "Offloads impact and toggles (scenario_07)",
  "collected_at": "2025-12-13T16:07:09.683145+00:00"
}
            ---
            # arp-requests cannot be seen by specific nodes

            ## Question
            I create an open ad-hoc wlan by using
```
iwconfig
```
 (I have the same issue with
```
wpa_supplicant
```
 as well). there are 4 nodes on the network as seen on the figure below. The nodes run ubuntu 12.04 and debian squeeze, and have 3.7.1, 3.5 and 3.2 kernels. I use two different usb dongle brands (TP link and ZCN) that all have AR9271 chipset and
```
ath9k_htc
```
 driver (here is lsusb output and ethtool output).
The problem I am experiencing is that two nodes (
```
10.0.0.2
```
 and
```
10.0.0.5
```
) which have TP link usb wifi dongles can ping any node on the network, and vice-versa. However, the other nodes (
```
10.0.0.6
```
 and
```
10.0.0.7
```
) that have ZCN wifi dongle cannot ping each other, but they have no problem communicating with TP-link wifi modules.
```
tcpdump
```
 shows that
```
10.0.0.6
```
 and
```
10.0.0.7
```
 cannot see their arp-request, e.g.
```
```
20:37:52.470305 ARP, Request who-has 10.0.0.7 tell 10.0.0.6, length 28
20:37:53.463713 ARP, Request who-has 10.0.0.7 tell 10.0.0.6, length 28
20:37:54.463622 ARP, Request who-has 10.0.0.7 tell 10.0.0.6, length 28
20:37:55.472868 ARP, Request who-has 10.0.0.7 tell 10.0.0.6, length 28
20:37:56.463439 ARP, Request who-has 10.0.0.7 tell 10.0.0.6, length 28
20:37:57.463469 ARP, Request who-has 10.0.0.7 tell 10.0.0.6, length 28
```
```
but they are able to see and get reply from TP-link's modules.
```
```
20:39:23.634459 ARP, Request who-has 10.0.0.2 tell 10.0.0.6, length 28
20:39:23.634551 ARP, Reply 10.0.0.2 is-at 64:70:02:18:d4:6a (oui Unknown), length 28
20:39:23.636687 IP 10.0.0.6 > 10.0.0.2: ICMP echo request, id 572, seq 1, length 64
20:39:23.636809 IP 10.0.0.2 > 10.0.0.6: ICMP echo reply, id 572, seq 1, length 64
20:39:24.635497 IP 10.0.0.6 > 10.0.0.2: ICMP echo request, id 572, seq 2, length 64
20:39:24.635558 IP 10.0.0.2 > 10.0.0.6: ICMP echo reply, id 572, seq 2, length 64
20:39:28.651946 ARP, Request who-has 10.0.0.6 tell 10.0.0.2, length 28
20:39:28.654021 ARP, Reply 10.0.0.6 is-at 00:19:70:94:7c:8b (oui Unknown), length 28
```
```
My question is that what could be the reason that
```
10.0.0.6
```
 and
```
10.0.0.7
```
 cannot see the
```
arp-request
```
 that they send each other? How can I find out the problem?
If I add couple more nodes with ZCN wifi dongle on the network, these nodes are also not able to talk with each other, but they are fine with TP-link. Or if I swap the wifi modules, the nodes with ZCN have always problem but TP-link modules are fine.
here is the
```
/etc/network/interfaces
```
,
```
ifconfig
```
,
```
iwconfig
```
,
```
ip a
```
,
```
ip r
```
,
```
route
```
 outputs
EDIT: I was suspecting if the problem is
```
arp_filter
```
 related but
```
/proc/sys/net/ipv4/conf/*/arp_filter
```
 is
```
0
```
 on the all subdomains(*). If I add arp info of
```
10.0.0.6
```
 and
```
10.0.0.7
```
 manually on these nodes,
```
tcpdump
```
 and
```
wireshark
```
 does not show that they send
```
ping
```
 to each other. If I
```
ping
```
 the broadcast address (10.0.0.255 in my case),
```
10.0.0.6
```
 and
```
10.0.0.7
```
 are able hear it.
EDIT2: Here is pcap files http://filebin.net/6cle9a5iae from
```
10.0.0.6
```
 (ZCN module),
```
10.0.0.7
```
 (ZCN module), and
```
10.0.0.5
```
 (TP-link module that does not have problem). here is the ping outputs from
```
10.0.0.6
```
http://pastebin.com/swFP2CJ9 I captured the packages simultaneously. The link also includes
```
ifconfig
```
;
```
iwconfig
```
; and
```
uname- a
```
 outputs for each node.

            ## Accepted Answer
            I had the same problem recently. I figured out that AR9271 chipset's have problem on onboard transmitter antenna. If you use an external antenna, then you will not have a problem. And this problem only occurs on ad-hoc mode.
The reason you don't experience problem with the TP-link should be that these modules uses external antenna which overcomes the chipset's problem, and ZCN modules should not have an external antenna.

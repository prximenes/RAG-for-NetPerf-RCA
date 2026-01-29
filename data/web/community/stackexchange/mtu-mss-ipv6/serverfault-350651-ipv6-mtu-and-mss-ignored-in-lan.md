---
            {
  "source": "stackexchange",
  "license": "CC BY-SA 4.0 (Stack Exchange)",
  "site": "serverfault",
  "question_id": 350651,
  "link": "https://serverfault.com/questions/350651/ipv6-mtu-and-mss-ignored-in-lan",
  "score": 1,
  "views": 624,
  "answer_id": 350779,
  "tags": [
    "routing",
    "ipv6",
    "linux-networking"
  ],
  "query_label": "mtu-mss-ipv6",
  "description": "IPv6 MTU/MSS discussion; supports fragmentation/PMTUD diagnostics",
  "collected_at": "2025-12-13T15:57:35.546185+00:00"
}
            ---
            # IPv6 MTU and MSS ignored in LAN?

            ## Question
            I have a server with a (sixxs) IPv6 tunnel and a local network behind it. The tunnel has MTU of 1470, and a prefix with this MTU is advertised by radvd, and picked up by the local client:
```
```
root@host:~# ip -6 route
2001:xxxx:xxxx::/64 dev eth1  proto kernel  metric 256  expires 298sec mtu 1470
fe80::/64 dev eth1  proto kernel  metric 256  mtu 1470
default via fe80::dad3:85ff:feaf:7e77 dev eth1  proto kernel  metric 1024  expires 28sec mtu 1470 hoplimit 64
```
```
The interface of the client has MTU of 1500, as usual. Now, when I transfer a file to a remote IPv6 host, the following happens (wireshark packet dump on the server, LAN interface, of relevant part):
```
```
15.034320 host -> remote SSHv2 Encrypted request packet len=2796
15.034408 server -> host ICMPv6 Too big
15.241163 host -> remote SSHv2 [TCP Retransmission] Encrypted request packet len=1398
15.252193 remote -> host TCP ssh > 58188 [ACK] Seq=2658 Ack=121902 Win=64128 Len=0 TSV=2205083594 TSER=4294965684
15.252480 host -> remote SSHv2 [TCP Retransmission] Encrypted request packet len=2796
15.252558 server -> host ICMPv6 Too big
15.461151 host -> remote SSHv2 [TCP Retransmission] Encrypted request packet len=1398
```
```
So, the host sends a packet of size 2796 (should not even be possible, the link MTU is 1500), and the server correctly replies with ICMPv6 Too big. The packet is then re-transmitted with the correct size and acknowledged. But then, the next packet is again too big, and the process repeats indefinitely, while the file is transferred at a snail's pace... What is happening here? The route cache shows that the MTU of the route is picked up correctly (IPv6 addresses replaced with names):
```
```
root@host:~# ip -6 route show cached
remote via fe80::dad3:85ff:feaf:7e77 dev eth1  metric 0
    cache  mtu 1470 hoplimit 64
server via server dev eth1  metric 0
    cache  mtu 1470
```
```

            ## Accepted Answer
            Okay, at home more weird issues were happening in the network. I took the Microsoft way and rebooted the server. Problem seems gone.

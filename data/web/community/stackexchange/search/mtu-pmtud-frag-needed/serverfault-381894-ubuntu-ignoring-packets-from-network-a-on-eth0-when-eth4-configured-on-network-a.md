---
            {
  "source": "stackexchange",
  "license": "CC BY-SA 4.0 (Stack Exchange)",
  "site": "serverfault",
  "question_id": 381894,
  "link": "https://serverfault.com/questions/381894/ubuntu-ignoring-packets-from-network-a-on-eth0-when-eth4-configured-on-network-a",
  "score": 4,
  "views": 6813,
  "answer_id": 381905,
  "answer_kind": "accepted",
  "tags": [
    "linux",
    "networking",
    "routing",
    "linux-networking",
    "nic"
  ],
  "query_label": "mtu-pmtud-frag-needed",
  "description": "PMTUD and MTU mismatch diagnostics (scenario_05)",
  "collected_at": "2025-12-13T16:07:03.868307+00:00"
}
            ---
            # Ubuntu Ignoring packets from network A on eth0 when eth4 configured on network A

            ## Question
            I have an Ubuntu 12.04 (final beta, up-to-date) server with two configured network interfaces:
```
```
root@mac:/home/sysadm# ifconfig
eth0      Link encap:Ethernet  HWaddr 00:1e:4f:28:fd:7b
          inet addr:172.18.8.10  Bcast:172.18.8.255  Mask:255.255.255.0
          inet6 addr: fe80::21e:4fff:fe28:fd7b/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:3362 errors:0 dropped:0 overruns:0 frame:0
          TX packets:8561 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:273506 (273.5 KB)  TX bytes:3174766 (3.1 MB)
          Interrupt:38 Memory:dc000000-dc012800
eth4      Link encap:Ethernet  HWaddr 00:02:c9:09:a4:c8
          inet addr:xxx.yy.4.235  Bcast:xxx.yy.5.255  Mask:255.255.254.0
          inet6 addr: fe80::202:c9ff:fe09:a4c8/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:59277 errors:0 dropped:52 overruns:0 frame:0
          TX packets:34 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:5138237 (5.1 MB)  TX bytes:6462 (6.4 KB)
lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:16436  Metric:1
          RX packets:1412 errors:0 dropped:0 overruns:0 frame:0
          TX packets:1412 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:107356 (107.3 KB)  TX bytes:107356 (107.3 KB)
root@mac:/home/sysadm# route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         172.18.8.254    0.0.0.0         UG    100    0        0 eth0
xxx.yy.4.0      0.0.0.0         255.255.254.0   U     0      0        0 eth4
172.18.8.0      0.0.0.0         255.255.255.0   U     0      0        0 eth0
```
```
As you can see, eth0 is on the 172.18.8.0/24 network ("8-net") and eth4 is on the xxx.yy.4.0/23 network ("4-net"). Both these networks are connected via a router. Many machines are on both networks (one at a time) and are able to communicate without problems. When a second machine on the 4-net attempts to talk to 172.18.8.10, the packets seem to be dropped. A tcpdump of an SSH attempt is below:
```
```
root@mac:/home/sysadm# ufw allow from any to any port 1022
Rule added
Rule added (v6)
root@mac:/home/sysadm# sshd -de -p 1022
sshd re-exec requires execution with an absolute path
root@mac:/home/sysadm# which sshd
/usr/sbin/sshd
root@mac:/home/sysadm# /usr/sbin/sshd -de -p 1022
debug1: sshd version OpenSSH_5.9p1 Debian-5ubuntu1
debug1: read PEM private key done: type RSA
debug1: Checking blacklist file /usr/share/ssh/blacklist.RSA-2048
debug1: Checking blacklist file /etc/ssh/blacklist.RSA-2048
debug1: private host key: #0 type 1 RSA
debug1: read PEM private key done: type DSA
debug1: Checking blacklist file /usr/share/ssh/blacklist.DSA-1024
debug1: Checking blacklist file /etc/ssh/blacklist.DSA-1024
debug1: private host key: #1 type 2 DSA
debug1: read PEM private key done: type ECDSA
debug1: Checking blacklist file /usr/share/ssh/blacklist.ECDSA-256
debug1: Checking blacklist file /etc/ssh/blacklist.ECDSA-256
debug1: private host key: #2 type 3 ECDSA
debug1: rexec_argv[0]='/usr/sbin/sshd'
debug1: rexec_argv[1]='-de'
debug1: rexec_argv[2]='-p'
debug1: rexec_argv[3]='1022'
Set /proc/self/oom_score_adj from 0 to -1000
debug1: Bind to port 1022 on 0.0.0.0.
Server listening on 0.0.0.0 port 1022.
debug1: Bind to port 1022 on ::.
Server listening on :: port 1022.
^Z
[1]+  Stopped                 /usr/sbin/sshd -de -p 1022
root@mac:/home/sysadm# bg
[1]+ /usr/sbin/sshd -de -p 1022 &
root@mac:/home/sysadm# tcpdump -nvlli eth0 'host xxx.yy.4.29'
tcpdump: listening on eth0, link-type EN10MB (Ethernet), capture size 65535 bytes
18:16:33.370081 IP (tos 0x0, ttl 63, id 29087, offset 0, flags [DF], proto TCP (6), length 60)
    xxx.yy.4.29.42667 > 172.18.8.10.1022: Flags [S], cksum 0xdc29 (correct), seq 107513294, win 14600, options [mss 1460,sackOK,TS val 3473994833 ecr 0,nop,wscale 7], length 0
18:16:36.369860 IP (tos 0x0, ttl 63, id 29088, offset 0, flags [DF], proto TCP (6), length 60)
    xxx.yy.4.29.42667 > 172.18.8.10.1022: Flags [S], cksum 0xd071 (correct), seq 107513294, win 14600, options [mss 1460,sackOK,TS val 3473997833 ecr 0,nop,wscale 7], length 0
18:16:42.369300 IP (tos 0x0, ttl 63, id 29089, offset 0, flags [DF], proto TCP (6), length 60)
    xxx.yy.4.29.42667 > 172.18.8.10.1022: Flags [S], cksum 0xb901 (correct), seq 107513294, win 14600, options [mss 1460,sackOK,TS val 3474003833 ecr 0,nop,wscale 7], length 0
```
```
For completeness:
```
```
root@mac:/home/sysadm# ufw status
Status: active
To                         Action      From
--                         ------      ----
22                         ALLOW       Anywhere
1022                       ALLOW       Anywhere
22                         ALLOW       Anywhere (v6)
1022                       ALLOW       Anywhere (v6)
```
```
The node making the connection experiences a timeout. Other protocols are also affected. Echo requests time out. However, nodes on the 8-net and all other networks that aren't the 4-net are able to communicate flawlessly. Logs do not show anything. Other "UFW BLOCK" entries exist in /var/log/syslog but no relevant ones exist.
In short, a machine has two interfaces, eth0 on network 8 and eth4 on network 4. Other nodes from network 4 cannot communicate with eth0 but nodes from all other networks can. The logical opposite also applies: network 8 nodes trying to talk to eth4 experience timeouts. Is this a feature or a bug? Should I just not expect to be able to talk to the logically wrong interface on a machine with two interfaces?
If it matters, this is a Dell PowerEdge R900. eth0 is an integrated port "NetXtreme II BCM5708 Gigabit Ethernet" and eth4 is one of two ports on an add-in card "MT26448 [ConnectX EN 10GigE, PCIe 2.0 5GT/s]" by Mellanox Technologies.
EDIT: Issue persists when the firewall is disabled. tcpdump still shows packets coming in (echo requests) with no responses being sent out.
EDIT: More output: This is a dump of eth4 traffic involving the remote host 'xxx.yy.4.29'. From xxx.yy.4.29, I pinged 172.18.8.10 and xxx.yy.4.235. This is the output.
```
```
root@mac:/home/sysadm# tcpdump -nvlli eth4 'host xxx.yy.4.29'
tcpdump: listening on eth4, link-type EN10MB (Ethernet), capture size 65535 bytes
20:25:04.401449 ARP, Ethernet (len 6), IPv4 (len 4), Request who-has xxx.yy.4.235 tell xxx.yy.4.29, length 46
20:25:04.401492 ARP, Ethernet (len 6), IPv4 (len 4), Reply xxx.yy.4.235 is-at 00:02:c9:09:a4:c8, length 28
20:25:04.401647 IP (tos 0x0, ttl 64, id 0, offset 0, flags [DF], proto ICMP (1), length 84)
    xxx.yy.4.29 > xxx.yy.4.235: ICMP echo request, id 32312, seq 1, length 64
20:25:04.401706 IP (tos 0x0, ttl 64, id 42264, offset 0, flags [none], proto ICMP (1), length 84)
    xxx.yy.4.235 > xxx.yy.4.29: ICMP echo reply, id 32312, seq 1, length 64
20:25:05.401200 IP (tos 0x0, ttl 64, id 0, offset 0, flags [DF], proto ICMP (1), length 84)
    xxx.yy.4.29 > xxx.yy.4.235: ICMP echo request, id 32312, seq 2, length 64
20:25:05.401211 IP (tos 0x0, ttl 64, id 42265, offset 0, flags [none], proto ICMP (1), length 84)
    xxx.yy.4.235 > xxx.yy.4.29: ICMP echo reply, id 32312, seq 2, length 64
20:25:09.402234 ARP, Ethernet (len 6), IPv4 (len 4), Request who-has xxx.yy.4.29 tell xxx.yy.4.235, length 28
20:25:09.402383 ARP, Ethernet (len 6), IPv4 (len 4), Reply xxx.yy.4.29 is-at 78:2b:cb:90:95:98, length 46
20:25:09.402747 ARP, Ethernet (len 6), IPv4 (len 4), Reply xxx.yy.4.29 is-at 78:2b:cb:90:95:98, length 46
```
```
EDIT: This is just a test machine. I cannot imagine a real-world scenario where I would need to route 8-net communication over the 4-net interface. I can see how this would be a known-issue where the benefit of a solution is not worth the effort of solving the problem.

            ## Accepted Answer
            What you're probably seeing here is reverse path filtering. The kernel is discarding packets because they seem to come from the "wrong" interface. To check if RPF is enabled, run
```
cat /proc/sys/net/ipv4/conf/eth0/rp_filter
```
 (and similarly for eth4). To disable it, echo 0 into thoses files.
Even with RPF disabled, your routing is going to be a bit weird as @NathanG said (the response packets will go out a different interface than they came in on). If your routers aren't too clever (i.e. don't have RPF or other spoof protection) this should still work though.
What you need to set this up properly is some policy routing based on the source address (i.e. tell the kernel to route packets differently based on their source address). We do this by setting up multiple routing tables, and then adding some rules to select which table to use.
First, name some tables (you only need to do this once).
```
```
echo "14 net4" >> /etc/iproute2/rt_tables
echo "18 net8" >> /etc/iproute2/rt_tables
```
```
Then add routes to these new tables (I'm assuming that this machine can access the Internet via routers on either eth0 or eth4).
```
```
ip route add xx.yy.4.0/23 dev eth4 table net4
ip route add default via xx.yy.4.1 table net4
ip route add 172.18.8.0/24 dev eth0 table net8
ip route add default via 172.18.8.254 table net8
```
```
And finally add some rules to select the appropriate table based on the source adderess of the packet.
```
```
ip rule add from xx.yy.4.0/23 lookup net4
ip rule add from 172.18.8.0/24 lookup net8
```
```

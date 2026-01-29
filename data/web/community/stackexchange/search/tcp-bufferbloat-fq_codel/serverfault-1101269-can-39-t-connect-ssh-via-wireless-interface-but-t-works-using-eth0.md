---
            {
  "source": "stackexchange",
  "license": "CC BY-SA 4.0 (Stack Exchange)",
  "site": "serverfault",
  "question_id": 1101269,
  "link": "https://serverfault.com/questions/1101269/cant-connect-ssh-via-wireless-interface-but-t-works-using-eth0",
  "score": 3,
  "views": 19904,
  "answer_id": 1108187,
  "answer_kind": "accepted",
  "tags": [
    "ssh",
    "linux-networking",
    "router",
    "wifi",
    "ethernet"
  ],
  "query_label": "tcp-bufferbloat-fq_codel",
  "description": "Bufferbloat and fq_codel/codel tuning (scenario_02)",
  "collected_at": "2025-12-13T16:07:01.453813+00:00"
}
            ---
            # Can&#39;t connect ssh via wireless interface but t works using eth0

            ## Question
            Suddenly I can't connect via
```
ssh
```
 to a server using my wireless interface but I can do it using the eth0 interface with a cable connected directly to my router.
From my wireless interface I got:
```
```
$ ssh -vvv my_server
OpenSSH_8.9p1 Ubuntu-3, OpenSSL 3.0.2 15 Mar 2022
debug1: Reading configuration data /home/user/.ssh/config
debug1: /home/user/.ssh/config line 38: Applying options for my_server
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 19: include /etc/ssh/ssh_config.d/*.conf matched no files
debug1: /etc/ssh/ssh_config line 21: Applying options for *
debug2: resolve_canonicalize: hostname XX.XXX.XX.XXX is address
debug3: expanded UserKnownHostsFile '~/.ssh/known_hosts' -> '/home/user/.ssh/known_hosts'
debug3: expanded UserKnownHostsFile '~/.ssh/known_hosts2' -> '/home/user/.ssh/known_hosts2'
debug3: ssh_connect_direct: entering
debug1: Connecting to XX.XXX.XX.XXX [XX.XXX.XX.XXX] port 22.
debug3: set_sock_tos: set socket 3 IP_TOS 0x10
debug1: connect to address XX.XXX.XX.XXX port 22: Network is unreachable
ssh: connect to host XX.XXX.XX.XXX port 22: Network is unreachable
```
```
and the
```
tcpdump
```
 is:
```
```
$ sudo tcpdump -v -i any tcp port 22
tcpdump: data link type LINUX_SLL2
tcpdump: listening on any, link-type LINUX_SLL2 (Linux cooked v2), snapshot length 262144 bytes
19:56:14.312414 wlp0s20f3 Out IP (tos 0x10, ttl 64, id 25412, offset 0, flags [DF], proto TCP (6), length 60)
    myhost.52266 > ec2-XX-XXX-XX-XXX.eu-central-1.compute.amazonaws.com.ssh: Flags [S], cksum 0x36d4 (incorrect -> 0xcc4d), seq 1642097124, win 64240, options [mss 1460,sackOK,TS val 1123249955 ecr 0,nop,wscale 7], length 0
```
```
From my eth interface:
```
```
$ ssh -vvv my_server
OpenSSH_8.9p1 Ubuntu-3, OpenSSL 3.0.2 15 Mar 2022
debug1: Reading configuration data /home/user/.ssh/config
debug1: /home/user/.ssh/config line 38: Applying options for my_server
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 19: include /etc/ssh/ssh_config.d/*.conf matched no files
debug1: /etc/ssh/ssh_config line 21: Applying options for *
debug2: resolve_canonicalize: hostname XX.XXX.XX.XXX is address
debug3: expanded UserKnownHostsFile '~/.ssh/known_hosts' -> '/home/user/.ssh/known_hosts'
debug3: expanded UserKnownHostsFile '~/.ssh/known_hosts2' -> '/home/user/.ssh/known_hosts2'
debug3: ssh_connect_direct: entering
debug1: Connecting to XX.XXX.XX.XXX [XX.XXX.XX.XXX] port 22.
debug3: set_sock_tos: set socket 3 IP_TOS 0x10
debug1: Connection established.
```
```
and the
```
tcpdump
```
 is:
```
```
$ sudo tcpdump -v -i any tcp port 22
tcpdump: data link type LINUX_SLL2
tcpdump: listening on any, link-type LINUX_SLL2 (Linux cooked v2), snapshot length 262144 bytes
22:14:16.335219 enp0s31f6 Out IP (tos 0x10, ttl 64, id 48434, offset 0, flags [DF], proto TCP (6), length 60)
    ws5.51632 > ec2-XX.XXX.XX.XXX.eu-central-1.compute.amazonaws.com.ssh: Flags [S], cksum 0x36d1 (incorrect -> 0xdbb4), seq 1199071061, win 64240, options [mss 1460,sackOK,TS val 151306527 ecr 0,nop,wscale 7], length 0
22:14:16.390032 enp0s31f6 In  IP (tos 0x0, ttl 48, id 0, offset 0, flags [DF], proto TCP (6), length 60)
    ec2-XX.XXX.XX.XXX.eu-central-1.compute.amazonaws.com.ssh > ws5.51632: Flags [S.], cksum 0xdc56 (correct), seq 1641064052, ack 1199071062, win 62643, options [mss 1440,sackOK,TS val 2605867526 ecr 151306527,nop,wscale 7], length 0
22:14:16.390126 enp0s31f6 Out IP (tos 0x10, ttl 64, id 48435, offset 0, flags [DF], proto TCP (6), length 52)
    ws5.51632 > ec2-XX.XXX.XX.XXX.eu-central-1.compute.amazonaws.com.ssh: Flags [.], cksum 0x36c9 (incorrect -> 0xfd95), ack 1, win 502, options [nop,nop,TS val 151306582 ecr 2605867526], length 0
22:14:16.397623 enp0s31f6 Out IP (tos 0x10, ttl 64, id 48436, offset 0, flags [DF], proto TCP (6), length 84)
    ws5.51632 > ec2-XX.XXX.XX.XXX.eu-central-1.compute.amazonaws.com.ssh: Flags [P.], cksum 0x36e9 (incorrect -> 0x92b6), seq 1:33, ack 1, win 502, options [nop,nop,TS val 151306590 ecr 2605867526], length 32: SSH: SSH-2.0-OpenSSH_8.9p1 Ubuntu-3
```
```
My working interface is enp0s31f6 (former eth0):
```
```
2: enp0s31f6: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc fq_codel state DOWN group default qlen 1000
```
```
and the failed one is the wifi market with
```
noqueue
```
:
```
```
3: wlp0s20f3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
```
```
I find very interesting that the addresses are given as IPv4 addresses in my
```
~/.ssh/config
```
, but the log says TCP(6). I guess that means IPv6. I have tried to force it with the option
```
-4
```
 but the result is the same.
my
```
~/.ssh/config
```
 is:
```
```
Host $ ssh -vvv my_server
   Hostname XX.XXX.XX.XXX
   User ubuntu
   IdentityFile ~/.ssh/my_id.pem
```
```
with
```
ethtool -S wlp0s20f3
```
 I can see that there are no dropped packets in the connection.
Which may be the cause ?

            ## Accepted Answer
            I had the same
```
debug3: set_sock_tos: set socket 3 IP_TOS 0x10
```
 trace that you mention and turns out that, for my specific case, I solved it with this answer, which was related to how my router managed the QoS of the WiFi. Simply by adding the
```
-o IPQoS=none
```
 I was finally able to connect:
```
```
axel@PTT426:~$ ssh -o IPQoS=none -i ~/.ssh/id_ed25519 -vvv git@github.com
OpenSSH_8.9p1 Ubuntu-3, OpenSSL 3.0.2 15 Mar 2022
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 19: include /etc/ssh/ssh_config.d/*.conf matched no files
debug1: /etc/ssh/ssh_config line 21: Applying options for *
debug3: expanded UserKnownHostsFile '~/.ssh/known_hosts' -> '/home/axel/.ssh/known_hosts'
debug3: expanded UserKnownHostsFile '~/.ssh/known_hosts2' -> '/home/axel/.ssh/known_hosts2'
debug2: resolving "github.com" port 22
debug3: resolve_host: lookup github.com:22
debug3: ssh_connect_direct: entering
debug1: Connecting to github.com [140.82.121.3] port 22.
debug1: Connection established.
```
```
By adding this into the top of my
```
~/.ssh/config
```
 file I got if fixed for every
```
git
```
 and
```
ssh
```
 operations:
```
```
Host *
  IPQoS=none
```
```
Hope it helps! :)

---
            {
  "source": "stackexchange",
  "license": "CC BY-SA 4.0 (Stack Exchange)",
  "site": "serverfault",
  "question_id": 642981,
  "link": "https://serverfault.com/questions/642981/docker-containers-cant-resolve-dns-on-ubuntu-14-04-desktop-host",
  "score": 79,
  "views": 246689,
  "answer_id": 642984,
  "answer_kind": "accepted",
  "tags": [
    "ubuntu",
    "networking",
    "domain-name-system",
    "docker",
    "lxc"
  ],
  "query_label": "docker-bridge-iptables-latency",
  "description": "Docker bridge + iptables/netfilter overhead (scenarios_14-15)",
  "collected_at": "2025-12-13T16:07:13.446470+00:00"
}
            ---
            # Docker containers can&#39;t resolve DNS on Ubuntu 14.04 Desktop Host

            ## Question
            I'm running into a problem with my Docker containers on Ubuntu 14.04 LTS.
Docker worked fine for two days, and then suddenly I lost all network connectivity inside my containers. The error output below initially lead me to believe it was because apt-get is trying to resolve the DNS via IPv6.
I disabled IPv6 on my host machine and still, removed all images, pulled base ubuntu, and still ran into the problem.
I changed my /etc/resolve.conf nameservers from my local DNS server to Google's public DNS servers (8.8.8.8 and 8.8.4.4) and still have no luck. I also set the DNS to Google in the DOCKER_OPTS of /etc/default/docker and restarted docker.
I also tried pulling coreos, and yum could not resolve DNS either.
It's weird because while DNS does not work, I still get a response when I ping the same update servers that apt-get can't resolve.
I'm not behind a proxy, I'm on a very standard local network, and this version of Ubuntu is up to date and fresh (I installed two days ago to be closer to docker).
I've thoroughly researched this through other posts on stackoverflow and github issues, but haven't found any resolution. I'm out of ideas as to how to solve this problem, can anyone help?
Error Message
```
```
➜  arthouse git:(docker) ✗ docker build --no-cache .
Sending build context to Docker daemon 51.03 MB
Sending build context to Docker daemon
Step 0 : FROM ubuntu:14.04
 ---> 5506de2b643b
Step 1 : RUN apt-get update
 ---> Running in 845ae6abd1e0
Err http://archive.ubuntu.com trusty InRelease
Err http://archive.ubuntu.com trusty-updates InRelease
Err http://archive.ubuntu.com trusty-security InRelease
Err http://archive.ubuntu.com trusty-proposed InRelease
Err http://archive.ubuntu.com trusty Release.gpg
  Cannot initiate the connection to archive.ubuntu.com:80 (2001:67c:1360:8c01::19). - connect (101: Network is unreachable) [IP: 2001:67c:1360:8c01::19 80]
Err http://archive.ubuntu.com trusty-updates Release.gpg
  Cannot initiate the connection to archive.ubuntu.com:80 (2001:67c:1360:8c01::19). - connect (101: Network is unreachable) [IP: 2001:67c:1360:8c01::19 80]
Err http://archive.ubuntu.com trusty-security Release.gpg
  Cannot initiate the connection to archive.ubuntu.com:80 (2001:67c:1360:8c01::19). - connect (101: Network is unreachable) [IP: 2001:67c:1360:8c01::19 80]
Err http://archive.ubuntu.com trusty-proposed Release.gpg
  Cannot initiate the connection to archive.ubuntu.com:80 (2001:67c:1360:8c01::19). - connect (101: Network is unreachable) [IP: 2001:67c:1360:8c01::19 80]
Reading package lists...
W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/trusty/InRelease
W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/trusty-updates/InRelease
W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/trusty-security/InRelease
W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/trusty-proposed/InRelease
W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/trusty/Release.gpg  Cannot initiate the connection to archive.ubuntu.com:80 (2001:67c:1360:8c01::19). - connect (101: Network is unreachable) [IP: 2001:67c:1360:8c01::19 80]
W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/trusty-updates/Release.gpg  Cannot initiate the connection to archive.ubuntu.com:80 (2001:67c:1360:8c01::19). - connect (101: Network is unreachable) [IP: 2001:67c:1360:8c01::19 80]
W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/trusty-security/Release.gpg  Cannot initiate the connection to archive.ubuntu.com:80 (2001:67c:1360:8c01::19). - connect (101: Network is unreachable) [IP: 2001:67c:1360:8c01::19 80]
W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/trusty-proposed/Release.gpg  Cannot initiate the connection to archive.ubuntu.com:80 (2001:67c:1360:8c01::19). - connect (101: Network is unreachable) [IP: 2001:67c:1360:8c01::19 80]
W: Some index files failed to download. They have been ignored, or old ones used instead.
```
```
Container IFCONFIG/PING
```
```
➜  code  docker run -it ubuntu /bin/bash
root@7bc182bf87bb:/# ifconfig
eth0      Link encap:Ethernet  HWaddr 02:42:ac:11:00:04
          inet addr:172.17.0.4  Bcast:0.0.0.0  Mask:255.255.0.0
          inet6 addr: fe80::42:acff:fe11:4/64 Scope:Link
          UP BROADCAST RUNNING  MTU:1500  Metric:1
          RX packets:7 errors:0 dropped:0 overruns:0 frame:0
          TX packets:8 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:738 (738.0 B)  TX bytes:648 (648.0 B)
lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
root@7bc182bf87bb:/# ping google.com
PING google.com (74.125.226.0) 56(84) bytes of data.
64 bytes from lga15s42-in-f0.1e100.net (74.125.226.0): icmp_seq=1 ttl=56 time=12.3 ms
--- google.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 12.367/12.367/12.367/0.000 ms
root@7bc182bf87bb:/# ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=44 time=21.8 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=44 time=21.7 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=44 time=21.7 ms
```
```
Also, apt-get update fails when I force IPv4:
```
```
root@6d925cdf84ad:/# sudo apt-get update -o Acquire::ForceIPv4=true
Err http://archive.ubuntu.com trusty InRelease
Err http://archive.ubuntu.com trusty-updates InRelease
Err http://archive.ubuntu.com trusty-security InRelease
Err http://archive.ubuntu.com trusty-proposed InRelease
Err http://archive.ubuntu.com trusty Release.gpg
  Unable to connect to archive.ubuntu.com:http: [IP: 91.189.88.153 80]
Err http://archive.ubuntu.com trusty-updates Release.gpg
  Unable to connect to archive.ubuntu.com:http: [IP: 91.189.88.153 80]
Err http://archive.ubuntu.com trusty-security Release.gpg
  Unable to connect to archive.ubuntu.com:http: [IP: 91.189.88.153 80]
Err http://archive.ubuntu.com trusty-proposed Release.gpg
  Unable to connect to archive.ubuntu.com:http: [IP: 91.189.88.153 80]
Reading package lists... Done
W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/trusty/InRelease
```
```

            ## Accepted Answer
            Woo, I found a post on github that solved my problem.
After Steve K. pointed out that it wasn't actually a DNS issue and was a connectivity issue, I was able to find a post on github that described how to fix this problem.
Apparently the docker0 network bridge was hung up. Installing bridge-utils and running the following got my Docker in working order:
```
```
apt-get install bridge-utils
pkill docker
iptables -t nat -F
ifconfig docker0 down
brctl delbr docker0
service docker restart
```
```

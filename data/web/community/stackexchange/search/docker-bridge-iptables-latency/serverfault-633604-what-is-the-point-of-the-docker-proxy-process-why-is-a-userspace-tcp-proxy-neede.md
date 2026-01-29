---
            {
  "source": "stackexchange",
  "license": "CC BY-SA 4.0 (Stack Exchange)",
  "site": "serverfault",
  "question_id": 633604,
  "link": "https://serverfault.com/questions/633604/what-is-the-point-of-the-docker-proxy-process-why-is-a-userspace-tcp-proxy-need",
  "score": 36,
  "views": 19532,
  "answer_id": 638993,
  "answer_kind": "accepted",
  "tags": [
    "iptables",
    "docker"
  ],
  "query_label": "docker-bridge-iptables-latency",
  "description": "Docker bridge + iptables/netfilter overhead (scenarios_14-15)",
  "collected_at": "2025-12-13T16:07:13.875585+00:00"
}
            ---
            # What is the point of the docker-proxy process? Why is a userspace tcp proxy needed?

            ## Question
            I have noticed that there is docker-proxy process running for each published port. What is the purpose of this process? Why is a user space tcp proxy needed for this?
```
```
$ ps -Af | grep proxy
root      4776  1987  0 01:25 ?        00:00:00 docker-proxy -proto tcp -host-ip 127.0.0.1 -host-port 22222 -container-ip 172.17.0.2 -container-port 22
root      4829  1987  0 01:25 ?        00:00:00 docker-proxy -proto tcp -host-ip 127.0.0.1 -host-port 5555 -container-ip 172.17.0.3 -container-port 5555
```
```
and some related iptable rules created by docker:
```
```
$ sudo iptables -t nat -L -n -v
Chain PREROUTING (policy ACCEPT 1 packets, 263 bytes)
 pkts bytes target     prot opt in     out     source               destination
    0     0 DOCKER     all  --  *      *       0.0.0.0/0            0.0.0.0/0            ADDRTYPE match dst-type LOCAL
Chain INPUT (policy ACCEPT 1 packets, 263 bytes)
 pkts bytes target     prot opt in     out     source               destination
Chain OUTPUT (policy ACCEPT 1748 packets, 139K bytes)
 pkts bytes target     prot opt in     out     source               destination
   32  7200 DOCKER     all  --  *      *       0.0.0.0/0           !127.0.0.0/8          ADDRTYPE match dst-type LOCAL
Chain POSTROUTING (policy ACCEPT 1719 packets, 132K bytes)
 pkts bytes target     prot opt in     out     source               destination
   32  7200 MASQUERADE  all  --  *      !docker0  172.17.0.0/16        0.0.0.0/0
Chain DOCKER (2 references)
 pkts bytes target     prot opt in     out     source               destination
    0     0 DNAT       tcp  --  !docker0 *       0.0.0.0/0            127.0.0.1            tcp dpt:22222 to:172.17.0.2:22
    0     0 DNAT       tcp  --  !docker0 *       0.0.0.0/0            127.0.0.1            tcp dpt:5555 to:172.17.0.3:5555
```
```

            ## Accepted Answer
            Apparently there are some edge cases without a better workaround (for now):
- localhost<->localhost routing
- docker instance calling into itself via its published port
- and possibly more
https://github.com/docker/docker/issues/8356
UPDATE:
Since 1.7.0 (2015-06-16) the userland proxy can be disabled in favor of hairpin NAT using the daemon’s --userland-proxy=false flag.

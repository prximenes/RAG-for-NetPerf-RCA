---
            {
  "source": "stackexchange",
  "license": "CC BY-SA 4.0 (Stack Exchange)",
  "site": "serverfault",
  "question_id": 990793,
  "link": "https://serverfault.com/questions/990793/variable-number-of-lost-udp-packets-reported-by-iperf-linux-scheduling",
  "score": 0,
  "views": 708,
  "answer_id": 990937,
  "tags": [
    "linux-networking",
    "iperf",
    "dropped"
  ],
  "query_label": "linux-udp-loss-scheduling",
  "description": "iperf UDP loss variability and Linux scheduling/processing; supports softirq/packet-loss reasoning",
  "collected_at": "2025-12-13T15:57:33.637521+00:00"
}
            ---
            # variable number of lost UDP packets reported by iperf, linux scheduling?

            ## Question
            I am testing a connectivity with an iperf server (iperf version 2.0.13 (21 Jan 2019) pthreads) running on a Bananpi M2+ single-board computer (Debian, 5.1.1-BPI-Kernel #1 SM).  For different target bandwidths I observed different rates of packet drops. The number of dropped packets is low for very low and very high target bandwidth settings (below 1%). With medium values, however, the number of lost packets is very high (e.g. 29% of packets were lost at 400 Mbps). What could cause such behavior? (detailed results see below).
This is the only communication that takes place in the test network (therefore drops must occur on the target side).
I already tried to resize the UDP socket, but that didn't improve the results.
```
```
------------------------------------------------------------
Server listening on UDP port 5001
Receiving 1470 byte datagrams
UDP buffer size: 3.81 MByte (WARNING: requested 1.91 MByte)
------------------------------------------------------------
[  3] local 192.168.1.11 port 5001 connected with 192.168.1.201 port 37950
[ ID] Interval       Transfer     Bandwidth        Jitter   Lost/Total Datagrams
[  3]  0.0-10.0 sec  11.9 MBytes  10.0 Mbits/sec   0.195 ms    0/ 8504 (0%)
[  4] local 192.168.1.11 port 5001 connected with 192.168.1.201 port 32833
[  4]  0.0-10.0 sec   118 MBytes  98.9 Mbits/sec   0.306 ms  571/85034 (0.67%)
[  3] local 192.168.1.11 port 5001 connected with 192.168.1.201 port 56833
[  3]  0.0-10.0 sec   344 MBytes   288 Mbits/sec   0.053 ms 9951/255103 (3.9%)
[  4] local 192.168.1.11 port 5001 connected with 192.168.1.201 port 51751
[  4]  0.0-10.0 sec   337 MBytes   283 Mbits/sec   0.026 ms 99684/340136 (29%)
[  3] local 192.168.1.11 port 5001 connected with 192.168.1.201 port 53331
[  3]  0.0-10.0 sec   512 MBytes   429 Mbits/sec   0.018 ms 60157/425171 (14%)
[  4] local 192.168.1.11 port 5001 connected with 192.168.1.201 port 35110
[  4]  0.0-10.0 sec   832 MBytes   698 Mbits/sec   0.014 ms 1860/595239 (0.31%)
[  3] local 192.168.1.11 port 5001 connected with 192.168.1.201 port 52002
[  3]  0.0-10.0 sec  1.04 GBytes   897 Mbits/sec   0.013 ms 2895/765308 (0.38%)
```
```
UPDATE
for 400 Mbps when I run iperf as a process with the default priority I get the following results:
```
```
pi@bpi2:~$ iperf -s -u
------------------------------------------------------------
Server listening on UDP port 5001
Receiving 1470 byte datagrams
UDP buffer size: 25.0 MByte (default)
------------------------------------------------------------
[  3] local 192.168.1.11 port 5001 connected with 192.168.1.201 port 44269
[ ID] Interval       Transfer     Bandwidth        Jitter   Lost/Total Datagrams
[  3]  0.0-10.0 sec   379 MBytes   318 Mbits/sec   0.030 ms 69509/340136 (20%)
[  4] local 192.168.1.11 port 5001 connected with 192.168.1.201 port 53115
[  4]  0.0-10.0 sec   463 MBytes   389 Mbits/sec   0.022 ms 9715/340137 (2.9%)
[  3] local 192.168.1.11 port 5001 connected with 192.168.1.201 port 39077
[  3]  0.0-10.0 sec   431 MBytes   362 Mbits/sec   0.031 ms 32537/340136 (9.6%)
[  4] local 192.168.1.11 port 5001 connected with 192.168.1.201 port 47676
[  4]  0.0-10.0 sec   363 MBytes   305 Mbits/sec   0.029 ms 81019/340136 (24%)
[  3] local 192.168.1.11 port 5001 connected with 192.168.1.201 port 52106
[  3]  0.0-10.0 sec   407 MBytes   341 Mbits/sec   0.030 ms 49872/340136 (15%)
```
```
when I set the highest priority :
```
```
pi@bpi2:~$ sudo ionice -c 1 -n 0 nice -n -20 iperf -s -u
------------------------------------------------------------
Server listening on UDP port 5001
Receiving 1470 byte datagrams
UDP buffer size: 25.0 MByte (default)
------------------------------------------------------------
[  3] local 192.168.1.11 port 5001 connected with 192.168.1.201 port 59056
[ ID] Interval       Transfer     Bandwidth        Jitter   Lost/Total Datagrams
[  3]  0.0-10.0 sec   460 MBytes   386 Mbits/sec   0.022 ms 11665/340137 (3.4%)
[  4] local 192.168.1.11 port 5001 connected with 192.168.1.201 port 54558
[  4]  0.0-10.0 sec   450 MBytes   378 Mbits/sec   0.039 ms 18941/340137 (5.6%)
[  3] local 192.168.1.11 port 5001 connected with 192.168.1.201 port 34361
[  3]  0.0-10.0 sec   437 MBytes   366 Mbits/sec   0.029 ms 28662/340137 (8.4%)
[  4] local 192.168.1.11 port 5001 connected with 192.168.1.201 port 47201
[  4]  0.0-10.0 sec   474 MBytes   398 Mbits/sec   0.033 ms 1953/340136 (0.57%)
[  3] local 192.168.1.11 port 5001 connected with 192.168.1.201 port 34809
[  3]  0.0-10.0 sec   442 MBytes   371 Mbits/sec   0.030 ms 24886/340136 (7.3%)
[  4] local 192.168.1.11 port 5001 connected with 192.168.1.201 port 54412
[  4]  0.0-10.0 sec   429 MBytes   360 Mbits/sec   0.037 ms 34388/340138 (10%)
[  3] local 192.168.1.11 port 5001 connected with 192.168.1.201 port 55946
[  3]  0.0-10.0 sec   446 MBytes   374 Mbits/sec   0.034 ms 22341/340136 (6.6%)
```
```

            ## Accepted Answer
            In the meantime, I have managed to find the solution myself. The reason for this strange behavior of the iperf was not the application itself, but a faulty driver for the NIC (most likely problems with the correct setting of the GbE delay).
What helped was the complete reinstallation of the operating system and the switch to Armbian 4.19, which has the correct driver set. I managed to find the solution in the armbian forum, which provides really extensive information for anyone interested in allwinner h3 SoCs (as the one used in my BananaPi M2+, but also many other products).

---
            {
  "source": "stackexchange",
  "license": "CC BY-SA 4.0 (Stack Exchange)",
  "site": "stackoverflow",
  "question_id": 49044325,
  "link": "https://stackoverflow.com/questions/49044325/difference-between-rx-missed-rx-errors-and-rx-nombuf",
  "score": 3,
  "views": 7609,
  "answer_id": 49044520,
  "answer_kind": "top-voted",
  "tags": [
    "dpdk"
  ],
  "query_label": "dpdk-rx-drops-nombuf",
  "description": "DPDK RX drops/counters and common causes (scenarios_17,19)",
  "collected_at": "2025-12-13T16:07:16.402675+00:00"
}
            ---
            # Difference between RX-missed, RX-errors and RX-nombuf

            ## Question
            I got the NIC stats while using the testpmd (comes along with DPDK). But, i am not able to understand the meaning of the all the counter ( RX-missed, RX-errors and RX-nombuf).
Please let me know exactly in which scenario the above mentioned counters will be incremented ?
Below is sample stats of a NIC using testpmd
```
```
testpmd> show port stats all
######################## NIC statistics for port 0  ########################
RX-packets: 7467716    RX-missed: 9751220    RX-bytes:  11335992888
RX-errors: 0
RX-nombuf:  980047
TX-packets: 0          TX-errors: 0          TX-bytes:  0
Throughput (since last show)
Rx-pps:        40950
Tx-pps:            0
############################################################################
######################## NIC statistics for port 1  ########################
RX-packets: 0          RX-missed: 0          RX-bytes:  0
RX-errors: 0
RX-nombuf:  0
TX-packets: 7450911    TX-errors: 0          TX-bytes:  11310482898
Throughput (since last show)
Rx-pps:            0
Tx-pps:        40946
############################################################################
```
```

            ## Accepted Answer
            RX-missed
Total of RX packets dropped by the HW, because there are no available buffer (i.e. RX queues are full).
The main reason for full RX queues is a "slow" application, which is not able to process packets in a rate they arrive on interface.
RX-errors
Total number of erroneous received packets, i.e. packets with incorrect checksum, runts, giants etc.
RX-nombuf
Total number of RX mbuf allocation failures, i.e. RX packet was drop due to lack of free mbufs in the mempool.
Those counters are described here:
http://dpdk.org/doc/api/structrte__eth__stats.html

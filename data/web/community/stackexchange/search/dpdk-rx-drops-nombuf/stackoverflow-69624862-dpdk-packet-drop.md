---
            {
  "source": "stackexchange",
  "license": "CC BY-SA 4.0 (Stack Exchange)",
  "site": "stackoverflow",
  "question_id": 69624862,
  "link": "https://stackoverflow.com/questions/69624862/dpdk-packet-drop",
  "score": 2,
  "views": 3335,
  "answer_id": 69684735,
  "answer_kind": "accepted",
  "tags": [
    "c++",
    "network-programming",
    "packet-capture",
    "dpdk"
  ],
  "query_label": "dpdk-rx-drops-nombuf",
  "description": "DPDK RX drops/counters and common causes (scenarios_17,19)",
  "collected_at": "2025-12-13T16:07:16.839070+00:00"
}
            ---
            # DPDK packet drop?

            ## Question
            I am trying to debug a issue related to packet loss when using DPDK. When using the application without DPDK, there is no issue seen.
To explain:
I have a process A which receives packets from process B (from different server).
Initial issue:
When DPDK is enabled in process A, for first few seconds, the packet flow is fine, however after few minutes the process A stops receiving any packets.
What can be possible reason for this ? I have confirmed packets are being sent by process B.
To debug this:
I have enabled pdump feature in my application so that I can take packet capture using dpdk-pdump.
While debugging, I see that, the server is receiving packets when I check using dpdk-proc-info
```
```
[root@QVr740-6 app]# ./dpdk-proc-info   -- --stats -p 0x1
EAL: Cannot find resource for device
EAL: No legacy callbacks, legacy socket not created
  ######################## NIC statistics for port 0  ########################
  **RX-packets: 11595973**    RX-errors:  0           RX-bytes:  17231595358
  RX-nombuf:  0
  TX-packets: 0           TX-errors:  0           TX-bytes:  22
  ############################################################################
```
```
However, when I take try taking packet capture :
```
```
[root@QVr740-6 app]# ./dpdk-pdump -l 42,44,46  --   --pdump 'device_id=0000:18:00.1,queue=*,rx-dev=/home/cu1/nmurshed/capture.pcap'
EAL: Detected 56 lcore(s)
EAL: Detected 2 NUMA nodes
EAL: Multi-process socket /var/run/dpdk/rte/mp_socket_69588_2a3baabe32a56
EAL: Selected IOVA mode 'PA'
EAL: Probing VFIO support...
EAL: Probe PCI driver: net_i40e (8086:1572) device: 0000:18:00.1 (socket 0)
EAL: Probe PCI driver: net_i40e (8086:1572) device: 0000:18:00.2 (socket 0)
EAL: Cannot find resource for device
EAL: No legacy callbacks, legacy socket not created
Port 2 MAC: 02 70 63 61 70 01
 core (42), capture for (1) tuples
 - port 0 device (0000:18:00.1) queue 65535
^C
Signal 2 received, preparing to exit...
##### PDUMP DEBUG STATS #####
 -packets dequeued:                     0
 -packets transmitted to vdev:          0
 -packets freed:                        0
```
```
How to find out where these packets are dropping ?
I did confirm that dpdk-pdump works when issue is not seen.
Any hints will be valuable as I have been tearing my hair on this.
EDIT:
I missed something in the stats. I see that Rx-missed_errors keep increasing at an alarming rate when the issue occurs.
```
```
Wed Oct 20 18:47:46 PDT 2021
rx_missed_errors: 0
Wed Oct 20 18:47:47 PDT 2021
rx_missed_errors: 0
Wed Oct 20 18:47:48 PDT 2021
rx_missed_errors: 0
Wed Oct 20 18:47:49 PDT 2021
rx_missed_errors: 8216
Wed Oct 20 18:47:50 PDT 2021
rx_missed_errors: 32384
Wed Oct 20 18:47:51 PDT 2021
rx_missed_errors: 56510
Wed Oct 20 18:47:52 PDT 2021
rx_missed_errors: 80636
Wed Oct 20 18:47:53 PDT 2021
rx_missed_errors: 104762
Wed Oct 20 18:47:54 PDT 2021
rx_missed_errors: 128882
Wed Oct 20 18:47:55 PDT 2021
rx_missed_errors: 152960
Wed Oct 20 18:47:56 PDT 2021
rx_missed_errors: 177086
Wed Oct 20 18:47:57 PDT 2021```
I increased the rx/tx desc in  rte_eth_rx_queue_setup which delays the problem. Somehow, my application is not freeing the rx_desc.
Question.. is each packet received == 1 rx_desc?
Is it possible that my application takes too long time to process packet ? or is it like I am not freeing them ?
```
```

            ## Accepted Answer
            DPDK counter
```
rx_missed_errors
```
 infers these many packets were not processed which were received on the NIC. While
```
Rx-no-mbuf
```
 represents the counters which showcase packets that were not DMA to CPU-Memory due to the absence of MBUF buffers. Hence the error is mostly in application logic either
```
Spending too much time processing the packets
```
 or
```
recursive processing on the same MBUF array after rx_burst
```
.
[EDIT-1] Based on a couple of debugging attempts and pointers the issue is root caused to application logic. Summarizing the below
- For incoming ARP requests the packets are processed and ARP reply is sent out on the same MBUF and
```
rte_pktmbuf_free
```
 we called immediately right after
```
rte_Eth_tx_burst
```
 - Issue Fixed
- For IP packets, the IP header and UDP header are processed for the desired packet and necessary changes are made to the MBUF before transmission. - for certain conditions (count of packets) the logic enters to longer loops which stalls the function exit.
Note:
- Fixing the above 2 issues seems to solve the issue.
- Using DPDK-Pktgen to generate custom packets allows to narrow down specific code areas.

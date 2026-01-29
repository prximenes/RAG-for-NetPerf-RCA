---
            {
  "source": "stackexchange",
  "license": "CC BY-SA 4.0 (Stack Exchange)",
  "site": "serverfault",
  "question_id": 1028430,
  "link": "https://serverfault.com/questions/1028430/how-to-direct-flows-to-specific-vf-queue",
  "score": 0,
  "views": 570,
  "answer_id": 1028651,
  "tags": [
    "nic",
    "ethtool",
    "sr-iov"
  ],
  "query_label": "sriov-direct-flows-vf-queue",
  "description": "Directing flows to specific VF queue; helps interpret queueing/drops on SR-IOV",
  "collected_at": "2025-12-13T15:57:38.389576+00:00"
}
            ---
            # How to direct flows to specific vf queue?

            ## Question
            SR-IOV allows us to create a VF from PF, now I want to direct some flows to VF via Flow Director.
Here is
```
ethtool
```
 help message
```
```
action N
    Specifies the Rx queue to send packets to, or some other action.
    loc N
    Specify the location/ID to insert the rule. This will overwrite any rule present in that location and will not go through any of the rule ordering process.
    delete N
    Deletes the RX classification rule with the given ID.
```
```
I'm really confused about how to set the value of
```
action
```
 so that the flow matching filters can be directed to specific VF.

            ## Accepted Answer
            I have found the answer in DPDK Flow Bifurcation How-to Guide (Yes, the answer is not in
```
SR-IOV
```
 docs or
```
Ethtool
```
 docs, orz)
example:
```
```
ethtool -N eth1 flow-type udp4 src-ip 192.0.2.2 dst-ip 198.51.100.2 \
        action $queue_index_in_VF0
ethtool -N eth1 flow-type udp4 src-ip 198.51.100.2 dst-ip 192.0.2.2 \
        action $queue_index_in_VF1
```
```
Where:
```
$queue_index_in_VFn
```
: Bits 39:32 of the variable defines VF id + 1; the lower 32 bits indicates the queue index of the VF. Thus:
-
```
$queue_index_in_VF0 = (0x1 & 0xFF) << 32 + [queue index]
```
.
-
```
$queue_index_in_VF1 = (0x2 & 0xFF) << 32 + [queue index]
```
.
action value structure

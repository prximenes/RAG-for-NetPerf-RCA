---
            {
  "source": "stackexchange",
  "license": "CC BY-SA 4.0 (Stack Exchange)",
  "site": "stackoverflow",
  "question_id": 61666624,
  "link": "https://stackoverflow.com/questions/61666624/testing-xdp-vs-dpdk",
  "score": 12,
  "views": 9803,
  "answer_id": 61690905,
  "answer_kind": "accepted",
  "tags": [
    "cpu",
    "dpdk",
    "ebpf",
    "xdp-bpf"
  ],
  "query_label": "xdp-vs-dpdk",
  "description": "XDP vs DPDK performance trade-offs and testing (scenarios_16-20)",
  "collected_at": "2025-12-13T16:07:15.585766+00:00"
}
            ---
            # Testing XDP vs DPDK

            ## Question
            I do have some experience with DPDK but currently I'm reading many blogs about XDP. I am trying to compare both technologies and understand the differences between DPDK and XDP. This raises some questions. I hope someone can help me with the following questions:
- With DPDK I can map workers to CPU cores and isolate CPU cores which will be used by DPDK. In case of eBPF / XDP, which CPU cores are used? Are all available CPU cores used? Would it be possible to isolate CPU cores meant for eBPF / XDP programs?
- When I test the throughput from a DPDK application, I'm able to check whether ring buffers (mempools) are full so packets will be lost. But how can I check whether an eBPF / XDP program causes packet drops because the throughput is too high? I assume when an eBPF / XDP program takes too much time to process a packet, eventually you will see packet drops? (especially when sending 64B packets on a high rate to find the maximum number of packets that can be send)
Thank you in advance for your help!

            ## Accepted Answer
            With DPDK I can map workers to CPU cores and isolate CPU cores which will be used by DPDK. In case of eBPF / XDP, which CPU cores are used?
Answer: XDP with eBPF runs in kernel space, unlike DPDK user space.
Are all available CPU cores used?
Answer: Yes, but normally irqbalance or interrupt pinning will put the RX queue of the port on to specific core.
Would it be possible to isolate CPU cores meant for eBPF / XDP programs?
Answer: You are referring to
```
KERNEL_CMD_LINE
```
 option
```
isol
```
, the understanding is incorrect. As mentioned above you can pin the interrupt of RX queue forcing to run eBPF XDP on that core.
When I test the throughput from a DPDK application, I'm able to check whether ring buffers (mempools) are full so packets will be lost. But how can I check whether an eBPF / XDP program causes packet drops because the throughput is too high?
Answer: you have use a mix of NIC and eBPF counters to achieve the same
I assume when an eBPF / XDP program takes too much time to process a packet, eventually, you will see packet drops? (especially when sending 64B packets on a high rate to find the maximum number of packets that can be send)
Answer: not necessary true, best performance of XDP is with zero-copy Driver to user space. Running application thread on a separate core gives an almost comparable performance as DPDK (tested with 2 * 10Gbps - 95% of DPDK performance).

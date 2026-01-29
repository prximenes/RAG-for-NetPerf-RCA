---
            {
  "source": "stackexchange",
  "license": "CC BY-SA 4.0 (Stack Exchange)",
  "site": "serverfault",
  "question_id": 241421,
  "link": "https://serverfault.com/questions/241421/napi-vs-adaptive-interrupts",
  "score": 12,
  "views": 17126,
  "answer_id": 247310,
  "answer_kind": "accepted",
  "tags": [
    "linux-networking",
    "nic"
  ],
  "query_label": "offloads-tso-gro-gso",
  "description": "Offloads impact and toggles (scenario_07)",
  "collected_at": "2025-12-13T16:07:08.724395+00:00"
}
            ---
            # NAPI vs Adaptive Interrupts

            ## Question
            Could anyone please explain how two following technologies are used to mitigate interrupt overhead under high networking load?
- Adaptive-rx/Adaptive-tx, and
- NAPI;
I would appreciate an answer that explains the difference closer to linux kernel source level? Also I would like to hear how to force the NIC to polling/interrupt coalescing mode at load which is ~ 400Mbps.
More background:
The problem seems to be that bnx2 and e1000 drivers ignore "ethtool -C adaptive-rx on" command. This is probably because those drivers do not support adaptive interrupts. Albeit the Broadcom Programmer's reference manual says that this feature should be supported by BCM5709 NIC hardware.
So I decided to try NAPI and reduce weight from 64 to 16 in netif_napi_add() function call to force the NIC in polling mode under much lower load, but unfortunately that did not work out. I guess that NAPI does not need any special hardware support in NIC, is that correct?
The hardware I am using is BCM5709 NIC (it uses bnx2 driver). And OS is Ubuntu 10.04. The CPU is XEON 5620.

            ## Accepted Answer
            The main principle behind interrupt moderation is to generate less than one interrupt per received frame (or one interrupt per transmit frame completion), reducing the OS overhead encountered when servicing interrupts.  The BCM5709 controller supports a couple of methods in hardware for coalescing interrupts, including:
- Generate an interrupt after receiving X frames (rx-frames in ethtool)
- Generate an interrupt when no more frames are received after X usecs (rx-usecs in ethtool)
The problem with using these hardware methods is that you need to select them to optimize throughput or latency, you can't have both.  Generating one interrupt for each received frame (rx-frames = 1) minimizes latency, but it does so at a high cost in terms of interrupt service overhead.  Setting a larger value (say rx-frames = 10) reduces the number of CPU cycles consumed by generating only one interrupt for each ten frames received, but you'll also encounter a higher latency for the first frames in that group of ten.
The NAPI implementation attempts to leverage the fact that traffic comes in bunches, so that you generate an interrupt immediately on the first frame received, then you immediately switch into polling mode (i.e. disable interrupts) because more traffic will be close behind.  After you've polled for some number of frames (16 or 64 in your question) or some time interval, then the driver will re-enable interrupts and start over again.
If you have a predictable workload then fixed values can be selected for any of the above (NAPI, rx-frames, rx-usecs) that give you the right trade-off, but most workloads vary and you end up making some sacrifices.  This is where adaptive-rx/adaptive-tx come into play.  The idea there is that the driver constantly monitors the workload (frames received per second, frame size, etc.) and tunes the hardware interrupt coalescing scheme to optimize for latency in low traffic situations or optimize for throughput in high traffic situations. It's a cool theory but may be difficult to implement in practice.  Only a few drivers implement it (see http://fxr.watson.org/fxr/search?v=linux-2.6&string=use_adaptive_rx_coalesce) and the bnx2/e1000 drivers aren't on that list.
For a good description of how each ethtool coalescing field is supposed to work, have a look at the definitions for the ethtool_coalesce structure at the following address:
http://fxr.watson.org/fxr/source/include/linux/ethtool.h?v=linux-2.6#L111
For you particular situation (~400Mb/s throughput) I'd suggest tuning the rx-frames and the rx-usecs values for the best settings for your workload.  Look at both the overhead of the ISR as well as the sensitivity of your application (httpd? etc.) to latency.
Dave

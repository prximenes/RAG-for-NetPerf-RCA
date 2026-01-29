---
            {
  "source": "stackexchange",
  "license": "CC BY-SA 4.0 (Stack Exchange)",
  "site": "serverfault",
  "question_id": 232403,
  "link": "https://serverfault.com/questions/232403/distribute-ip-packets-accross-different-nic-queues-with-msi-message-signalled-i",
  "score": 2,
  "views": 1794,
  "answer_id": 234114,
  "answer_kind": "accepted",
  "tags": [
    "ipsec",
    "nic",
    "linux-networking",
    "msi",
    "interrupts"
  ],
  "query_label": "softirq-saturation",
  "description": "SoftIRQ saturation / ksoftirqd spikes (scenario_01)",
  "collected_at": "2025-12-13T16:07:00.263209+00:00"
}
            ---
            # Distribute IP packets accross different NIC queues with MSI (Message Signalled Interrupts)

            ## Question
            NetXtreme II BCM5709 Gigabit Ethernet NIC supports MSI feature (Message Signaled Interrupts) and it has 8 queues. Each queue has its own Interrupt handler in /proc/interrupts. What I am trying to accomplish is to tell NIC which packets should go to which queue.
Questions:
- Is it possible to manually specify which IP packets should go to which queue by encapsulated protocol type (e.g. IPsec packets go in one queue, while TCP packets go in another queue)?
- If it is possible - how can I do it under Linux?
- If it is not possible - should I look at MSI-X capable NIC cards to solve this problem?
More details:
We have one Interface that is terminating IPSec and forwarding/terminating TCP connections. The IPSec packet decryption is inlined (this means that decryption is done under the same ksoftirqd/X context). We are trying to find out if we will be able to improve total performance if IPSec packets will be scheduled on another CPU than TCP packets. One more limitation is that IPSec code is not MP-safe, hence I can not run it under more than one ksoftirqd/X. By default it seems that packets are distributed/hashed by source IP over the 8 NIC queues. The bottleneck is IPSec that chokes out TCP traffic while it is decrypting/encrypting IPSec packets at ~100% CPU under ksoftirqd/X context.
OS is Ubuntu 10.10 (2.6.32-27-server) and NIC is Broadcom BCM5709.

            ## Accepted Answer
            If someone else will be trying to find out how to make Linux Networking TCP/IP stack to scale on multiple CPU cores...
MSI can be exploited by two underlying NIC technologies to distribute packets across multiple queues. Each NIC queue is handled by a different Interrupt on a dedicated CPU core to achieve scalability:
- RSS (Receive Side Scaling) - distributes packets to different queues by Source and Destination IP and if applicable by TCP/UDP source and destination ports.
- VMDq (Virtual Machine Device queues) - distributes packets by MAC address or VLAN tags. Mostly used by VM hypervisors but I do not see any reason why it could not be used in non-VM setups.
The problem with RSS is that it always uses source IP to generate a hash. Hash is used to find to which queue this packet should go. This means that one can't control which packets should go to which queue unless he also has control over the source IPs.
VMDq seems to be more appropriate to my problem, because it distributes packets by destination MAC address. It could be as simple as assigning two different IP addresses to the same interface.
Source:
- http://www.broadcom.com/collateral/pg/NetXtremeII-PG203-R.pdf
- http://download.intel.com/design/network/manuals/316080.pdf

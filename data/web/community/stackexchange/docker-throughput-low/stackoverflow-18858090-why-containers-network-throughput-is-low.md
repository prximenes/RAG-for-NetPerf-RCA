---
            {
  "source": "stackexchange",
  "license": "CC BY-SA 4.0 (Stack Exchange)",
  "site": "stackoverflow",
  "question_id": 18858090,
  "link": "https://stackoverflow.com/questions/18858090/why-containers-network-throughput-is-low",
  "score": 3,
  "views": 2814,
  "answer_id": 18991326,
  "tags": [
    "performance",
    "network-programming",
    "throughput",
    "docker",
    "lxc"
  ],
  "query_label": "docker-throughput-low",
  "description": "Why container network throughput can be low; bridges/veth/NAT overhead and tuning hints",
  "collected_at": "2025-12-13T15:57:41.248796+00:00"
}
            ---
            # Why containers network throughput is low

            ## Question
            I created a couple of containers using Dockers and measured the network performance by means of Netperf. However the throughput results to be quite low, around 563.81 Mb/s. Isn't the communication between 2 containers/processes done through main memory? Does anyone have an idea why I am having such a low throughput. Do I need a specific configuration?
Thanks,
Genc

            ## Accepted Answer
            The question has been asked on the
```
docker-user
```
 mailing list, and after some investigation, we found out that performance of
```
veth
```
 in VMs with kernel 3.8 was "not great", and was significantly improved with kernel 3.10.
In other words:
- if you run containers on bare metal, you will be fine (and see very fast transfer speeds between containers), regardless of the kernel version that you are using;
- if you run containers in a VM (tested with Xen, VirtualBox, and KVM), you might see a huge drop in container-to-container transfer speed, if you run with kernel up to 3.8;
- if you run kernel 3.10 or above, performance will be fine, regardless of the setup.
We haven't pinpointed the source of the problem yet, though.

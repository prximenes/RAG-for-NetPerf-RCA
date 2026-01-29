---
            {
  "source": "stackexchange",
  "license": "CC BY-SA 4.0 (Stack Exchange)",
  "site": "serverfault",
  "question_id": 230495,
  "link": "https://serverfault.com/questions/230495/what-does-st-mean-in-top",
  "score": 36,
  "views": 34343,
  "answer_id": 230503,
  "answer_kind": "accepted",
  "tags": [
    "linux",
    "amazon-ec2",
    "cpu-usage",
    "top"
  ],
  "query_label": "cpu-steal-time",
  "description": "CPU steal time (%steal / %st) and latency spikes in guests (scenario_22)",
  "collected_at": "2025-12-13T16:07:12.060451+00:00"
}
            ---
            # What does %st mean in top?

            ## Question
            Here is an example from my top:
```
```
Cpu(s):  6.0%us,  3.0%sy,  0.0%ni, 78.7%id,  0.0%wa,  0.0%hi,  0.3%si, 12.0%st
```
```
I am trying to figure out the significance of the %st field. I read that it means steal cpu and it represents time spent by the hypervisor, but I want to know what that actually means to me.
Does it mean I may be on a busy physical server and someone else is using too much CPU on the server and they are taking from my VM?
If I am using EBS could it be related to handling EBS I/O at the hypervisor level?
Is it related to things running on my VM or is it completely unaffected by me?

            ## Accepted Answer
            The Steal percentage (documented in the
```
mpstat
```
 man-page) is indeed the hypervisor telling your VM that it can't have CPU resources the VM would otherwise use. This percentage is regulated in part by Amazon's CPU limiting, and VM load on that specific host. I/O load is monitored through the
```
%io
```
 stat.
You will see this most often on their
```
t
```
 class of instances that use a CPU credit model for regulating performance. If you're seeing high percentages, chances are good you're running out of CPU credits.

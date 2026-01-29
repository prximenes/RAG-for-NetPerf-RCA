---
            {
  "source": "stackexchange",
  "license": "CC BY-SA 4.0 (Stack Exchange)",
  "site": "serverfault",
  "question_id": 392216,
  "link": "https://serverfault.com/questions/392216/is-there-a-windows-equivalent-of-unix-cpu-steal-time",
  "score": 29,
  "views": 10823,
  "answer_id": 455554,
  "answer_kind": "accepted",
  "tags": [
    "windows",
    "amazon-ec2",
    "monitoring",
    "cpu-usage",
    "metrics"
  ],
  "query_label": "cpu-steal-time",
  "description": "CPU steal time (%steal / %st) and latency spikes in guests (scenario_22)",
  "collected_at": "2025-12-13T16:07:12.482647+00:00"
}
            ---
            # Is there a Windows equivalent of Unix &#39;CPU steal time&#39;?

            ## Question
            In order to assess performance monitoring accuracy on virtualization platforms, the CPU steal time has become an increasingly relevant metric - see EC2 monitoring: the case of stolen CPU for an instructive summary in the context of Amazon EC2 and IBM's paper on CPU time accounting for a more in-depth technical explanation (including illustrations) of the concept:
Steal time is the percentage of time a virtual CPU waits for a real
  CPU while the hypervisor is servicing another virtual processor.
Accordingly, it is exposed in most related Unix/Linux monitoring tools nowadays - see e.g. columns %steal or st in
```
sar
```
 or
```
top
```
:
st  --  Steal Time
  The amount of CPU 'stolen' from this virtual machine by the hypervisor
  for other tasks (such as running another virtual machine).
I've been unable to figure out how to capture the same metric on Windows though, is this possible already? (Ideally for the Windows 2008 Server R2 AMIs on EC2 and via a respective Windows Performance Counters of course.)

            ## Accepted Answer
            Edit: Updating on Oct. 1 2013 - Some of my original answer has since become obsolete.
I'm not sure if you're still active on this site or that you'll see this, but I wanted you to know that I read this question today and it fascinated me, and so I spent all day (when I should have been working) researching Hyper-V and Windows internals and even digging in to the very concepts of virtualization itself in hopes that I might be ready to answer your question.
Let me preface by saying that I am coming from the point of view of Hyper-V as a virtualization platform because that is where I have the most experience.  Even though there may be certain tenets of virtualization, as we know it, that cannot be deviated from, Microsoft and VMware and Xen all have different strategies for how they design their hypervisors.
That's the first thing that makes your question challenging.  You pose your question as if it were hypervisor-agnostic, when in truth it is not.  Amazon EC2, for example, uses the Xen hypervisor, and the "CPU Steal Time" metric that you see in the output of a
```
top
```
 command issued from within a Linux VM running on that hypervisor is a result of the integration services installed on that guest OS (or virtualization-aware tools on the guest) in conjunction with data provided by that specific hypervisor.
First off let me just answer your question straight up: There is no way to see from inside a virtual machine running Windows how much time the processors belonging to the physical machine on which the hypervisor runs spends doing other things, unless the particular virtual tools/services or virtualization-aware tools for your particular hypervisor are installed in the guest VM and the particular hypervisor on which the guest is running exposes that data to the guest.  Even a Windows guest running on a Hyper-V hypervisor will not have immediate access to information regarding the time spent that the physical processors on the hypervisor were doing other things.  (To quote voretaq7, something that "breaks the fourth wall.")  Even though Windows client and server operating systems running as virtualized guests in Hyper-V with the correct integration services/tools installed make use of "enlightenments" (which are literally kernel code alterations made especially for VMs) that significantly increase their performance in using the resources of a physical host, the bottom line is that the hypervisor does not have to give any more information to the guest OS than it wants to.  That means the hypervisor does not have to tell a guest VM what else it is doing besides servicing that VM... unless it wants to.  And that information about what else the physical processors are doing is necessary for deriving a metric from the perspective of the VM such as "CPU Steal Time: the percentage of time the vCPU waits for a physical CPU."
How could the guest OS know that, if it didn't even realize that it was actually virtualized?
In other words, without the right integration tools installed on the guest, the guest OS won't even know that its CPU is actually a vCPU.  It won't even know that there is another force outside of itself "stealing" CPU cycles from it, therefore that metric will not exist on the guest VM.
VMware has begun to expose this data to Windows guests as well as of ESXi 5.0. VMware integration tools also need to be updated on the guest. Here is a reference; they refer to it as "CPU Stolen Time".
A hypervisor such as Hyper-V does not give guests direct access to physical resources such as physical processors or processor cores.  Instead the hypervisor gives them vDevs - virtual devices - such as vCPUs.
A prime example of why: Say a virtual machine guest OS makes the call to flush the TLB (translation look-aside buffer) which is a physical component of a physical CPU.  If the guest OS was allowed to clear the entire TLB on a physical processor, that would have negative performance effects for all the other VMs that were also sharing that same physical TLB.  In the case of Windows, that call in the guest OS is translated into a "hypercall" or "enlightened" call which is interpreted by the hypervisor so that only the section of the TLB that is relevant to that virtual machine is flushed.
(Interestingly, that hints to me that guest VMs that do not have the proper integration tools and/or services could have the ability to impact the performance of all the other VMs on the same host, but that is completely outside the scope of this topic.)
All that to say that you can still detect in a Hyper-V host the time that a virtual processor spent waiting for a real processor to become available so that it could scheduled to run.  But you can only see that data on a Windows Hyper-V hypervisor.  If it is possible to see this in other hypervisors, I urge others to tell us how to see this in that hypervisor and also if it is exposed to the guests.  (Edit 10/1/2013 Thank you evilensky for doing just that!)
My test machine was Hyper-V Server 2012, which is the free edition of Server 2012 that only runs Core and the Hyper-V role.  It's effectively the same as any Windows Server 2012 running Hyper-V.
Fire up Perfmon on your parent partition, aka physical host.  Load this counter:
```
```
Hyper-V Hypervisor Virtual Processor\CPU Wait Time Per Dispatch\*
```
```
You will notice that there will be an instance of that counter for each virtual machine on that hypervisor, as well as _Total. The Microsoft definition of that Perfmon counter is:
The average time (in nanoseconds) spent waiting for a virtual processor to be dispatched onto a logical processor.
Obviously, you want that number to be as low as possible.  For computers, waiting is almost never a good thing.
Other performance counters on the hypervisor that you will want to investigate are
```
Hyper-V Hypervisor Root Virtual Processor\% Guest Run Time
```
,
```
% Hypervisor Run Time
```
, and
```
% Total Run Time
```
.  These counters provide you with the percentages that could be used to determine facts such as how much time the "real" processors spend doing things other than servicing a VM or all VMs.
So in conclusion, the metric that you are looking for in a guest virtual machine depends on the hypervisor that it is running on, whether that hypervisor chooses to provide the data about how it spends its time other than servicing that VM, and if the guest OS has the right virtualization integration tools/services/drivers to be aware enough to realize that the hypervisor is making that data available.
I know of no way on a Windows guest, integration tools installed or not, to see how much time, in terms of seconds or percentage, that VM's host has spent servicing it or not servicing it respective to the total physical processor time.(Edit 10/1/2013: ESXi 5.0 or better exposes this data to the guest VM through the integration tools. Still nothing on Hyper-V though.)

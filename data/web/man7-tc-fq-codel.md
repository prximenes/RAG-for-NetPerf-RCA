---
                {
  "source": "web",
  "label": "man7-tc-fq-codel",
  "url": "https://man7.org/linux/man-pages/man8/tc-fq_codel.8.html",
  "description": "fq_codel qdisc parameters used in bufferbloat scenarios",
  "license": null,
  "collected_at": "2025-12-15T17:15:22.194107+00:00"
}
                ---
                # tc-fq_codel(8) — Linux manual page

                tc-fq_codel(8) - Linux manual page
man7.org > Linux > man-pages
Linux/UNIX system programming training
tc-fq_codel(8) — Linux manual page
NAME | SYNOPSIS | DESCRIPTION | PARAMETERS | EXAMPLES | SEE ALSO | AUTHORS | COLOPHON
```
FQ_CoDel(8)                       Linux                       FQ_CoDel(8)
```
NAME          top
```
       CoDel - Fair Queuing (FQ) with Controlled Delay (CoDel)
```
SYNOPSIS          top
```
tc qdisc ... fq_codel [ limit PACKETS ] [ flows NUMBER ] [ target
       TIME ] [ interval TIME ] [ quantum BYTES ] [ ecn | noecn ] [
       ce_threshold TIME ] [ ce_threshold_selector VALUE/MASK ] [
       memory_limit BYTES ]
```
DESCRIPTION          top
```
       FQ_Codel (Fair Queuing Controlled Delay) is queuing discipline
       that combines Fair Queuing with the CoDel AQM scheme. FQ_Codel
       uses a stochastic model to classify incoming packets into
       different flows and is used to provide a fair share of the
       bandwidth to all the flows using the queue. Each such flow is
       managed by the CoDel queuing discipline. Reordering within a flow
       is avoided since Codel internally uses a FIFO queue.
```
PARAMETERS          top
```
limit
       has the same semantics as codel and is the hard limit on the real
       queue size.  When this limit is reached, incoming packets are
       dropped. Default is 10240 packets.
   memory_limit
       sets a limit on the total number of bytes that can be queued in
       this FQ-CoDel instance. The lower of the packet limit of the limit
       parameter and the memory limit will be enforced. Default is 32 MB.
   flows
       is the number of flows into which the incoming packets are
       classified. Due to the stochastic nature of hashing, multiple
       flows may end up being hashed into the same slot. Newer flows have
       priority over older ones. This parameter can be set only at load
       time since memory has to be allocated for the hash table.  Default
       value is 1024.
   target
       has the same semantics as codel and is the acceptable minimum
       standing/persistent queue delay. This minimum delay is identified
       by tracking the local minimum queue delay that packets experience.
       Default value is 5ms.
   interval
       has the same semantics as codel and is used to ensure that the
       measured minimum delay does not become too stale.  The minimum
       delay must be experienced in the last epoch of length interval.
       It should be set on the order of the worst-case RTT through the
       bottleneck to give endpoints sufficient time to react. Default
       value is 100ms.
   quantum
       is the number of bytes used as 'deficit' in the fair queuing
       algorithm. Default is set to 1514 bytes which corresponds to the
       Ethernet MTU plus the hardware header length of 14 bytes.
   ecn | noecn
       has the same semantics as codel and can be used to mark packets
       instead of dropping them. If ecn has been enabled, noecn can be
       used to turn it off and vice-a-versa. Unlike codel, ecn is turned
       on by default.
   ce_threshold
       sets a threshold above which all packets are marked with ECN
       Congestion Experienced. This is useful for DCTCP-style congestion
       control algorithms that require marking at very shallow queueing
       thresholds.
   ce_threshold_selector
       sets a filter so that the ce_threshold feature is applied to only
       a subset of the traffic seen by the qdisc. If set, the MASK value
       will be applied as a bitwise AND to the diffserv/ECN byte of the
       IP header, and only if the result of this masking equals VALUE,
       will the ce_threshold logic be applied to the packet.
   drop_batch
       sets the maximum number of packets to drop when limit or
       memory_limit is exceeded. Default value is 64.
```
EXAMPLES          top
```
       #tc qdisc add   dev eth0 root fq_codel
       #tc -s qdisc show
       qdisc fq_codel 8002: dev eth0 root refcnt 2 limit 10240p flows
       1024 quantum 1514
        target 5.0ms interval 100.0ms ecn
          Sent 428514 bytes 2269 pkt (dropped 0, overlimits 0 requeues 0)
          backlog 0b 0p requeues 0
           maxpacket 256 drop_overlimit 0 new_flow_count 0 ecn_mark 0
           new_flows_len 0 old_flows_len 0
       #tc qdisc add dev eth0 root fq_codel limit 2000 target 3ms
       interval 40ms noecn
       #tc -s qdisc show
       qdisc fq_codel 8003: dev eth0 root refcnt 2 limit 2000p flows 1024
       quantum 1514 target 3.0ms interval 40.0ms
        Sent 2588985006 bytes 1783629 pkt (dropped 0, overlimits 0
       requeues 34869)
        backlog 0b 0p requeues 34869
         maxpacket 65226 drop_overlimit 0 new_flow_count 73 ecn_mark 0
         new_flows_len 1 old_flows_len 3
```
SEE ALSO          top
```
tc(8), tc-codel(8), tc-red(8)
```
AUTHORS          top
```
       FQ_CoDel was implemented by Eric Dumazet. This manpage was written
       by Vijay Subramanian. Please report corrections to the Linux
       Networking mailing list <netdev@vger.kernel.org>.
```
COLOPHON          top
```
       This page is part of the iproute2 (utilities for controlling
       TCP/IP networking and traffic) project.  Information about the
       project can be found at
       â¨http://www.linuxfoundation.org/collaborate/workgroups/networking/iproute2â©.
       If you have a bug report for this manual page, send it to
       netdev@vger.kernel.org, shemminger@osdl.org.  This page was
       obtained from the project's upstream Git repository
       â¨https://git.kernel.org/pub/scm/network/iproute2/iproute2.gitâ© on
       2025-08-11.  (At that time, the date of the most recent commit
       that was found in the repository was 2025-08-08.)  If you discover
       any rendering problems in this HTML version of the page, or you
       believe there is a better or more up-to-date source for the page,
       or you have corrections or improvements to the information in this
       COLOPHON (which is not part of the original manual page), send a
       mail to man-pages@man7.org
iproute2                       4 June 2012                    FQ_CoDel(8)
```
Pages that refer to this page:
    ovs-vswitchd.conf.db(5),
    tc(8),
    tc-cake(8),
    tc-fq_pie(8)
            HTML rendering created 2025-09-06
            by Michael Kerrisk,
            author of
            The Linux Programming Interface.
            For details of in-depth
            Linux/UNIX system programming training courses
            that I teach, look here.
            Hosting by jambit GmbH.
var sc_project=7422636;
var sc_invisible=1;
var sc_security="9b6714ff";
  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-9830363-8']);
  _gaq.push(['_trackPageview']);
  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

---
                {
  "source": "web",
  "label": "man7-tc-codel",
  "url": "https://man7.org/linux/man-pages/man8/tc-codel.8.html",
  "description": "codel qdisc parameters used in AQM interpretation",
  "license": null,
  "collected_at": "2025-12-15T17:15:22.508487+00:00"
}
                ---
                # tc-codel(8) — Linux manual page

                tc-codel(8) - Linux manual page
man7.org > Linux > man-pages
Linux/UNIX system programming training
tc-codel(8) — Linux manual page
NAME | SYNOPSIS | DESCRIPTION | ALGORITHM | PARAMETERS | EXAMPLES | SEE ALSO | SOURCES | AUTHORS | COLOPHON
```
CoDel(8)                          Linux                          CoDel(8)
```
NAME          top
```
       CoDel - Controlled-Delay Active Queue Management algorithm
```
SYNOPSIS          top
```
tc qdisc ... codel [ limit PACKETS ] [ target TIME ] [ interval
       TIME ] [ ecn | noecn ] [ ce_threshold TIME ]
```
DESCRIPTION          top
```
       CoDel (pronounced "coddle") is an adaptive "no-knobs" active queue
       management algorithm (AQM) scheme that was developed to address
       the shortcomings of RED and its variants. It was developed with
       the following goals in mind:
       *   It should be parameterless.
       *   It should keep delays low while permitting bursts of traffic.
       *   It should control delay.
       *   It should adapt dynamically to changing link rates with no
           impact on utilization.
       *   It should be simple and efficient and should scale from simple
           to complex routers.
```
ALGORITHM          top
```
       CoDel comes with three major innovations. Instead of using queue
       size or queue average, it uses the local minimum queue as a
       measure of the standing/persistent queue.  Second, it uses a
       single state-tracking variable of the minimum delay to see where
       it is relative to the standing queue delay. Third, instead of
       measuring queue size in bytes or packets, it is measured in
       packet-sojourn time in the queue.
       CoDel measures the minimum local queue delay (i.e. standing queue
       delay) and compares it to the value of the given acceptable queue
       delay target.  As long as the minimum queue delay is less than
       target or the buffer contains fewer than MTU worth of bytes,
       packets are not dropped.  Codel enters a dropping mode when the
       minimum queue delay has exceeded target for a time greater than
       interval.  In this mode, packets are dropped at different drop
       times which is set by a control law. The control law ensures that
       the packet drops cause a linear change in the throughput. Once the
       minimum delay goes below target, packets are no longer dropped.
       Additional details can be found in the paper cited below.
```
PARAMETERS          top
```
limit
       is the hard limit on the real queue size. When this limit is
       reached, incoming packets are dropped. If the value is lowered,
       packets are dropped so that the new limit is met. Default is 1000
       packets.
   target
       is the acceptable minimum standing/persistent queue delay. This
       minimum delay is identified by tracking the local minimum queue
       delay that packets experience.  Default and recommended value is
       5ms.
   interval
       is used to ensure that the measured minimum delay does not become
       too stale. The minimum delay must be experienced in the last epoch
       of length interval.  It should be set on the order of the worst-
       case RTT through the bottleneck to give endpoints sufficient time
       to react. Default value is 100ms.
   ecn | noecn
       can be used to mark packets instead of dropping them. If ecn has
       been enabled, noecn can be used to turn it off and vice-a-versa.
       By default, ecn is turned off.
   ce_threshold
       sets a threshold above which all packets are marked with ECN
       Congestion Experienced. This is useful for DCTCP-style congestion
       control algorithms that require marking at very shallow queueing
       thresholds.
```
EXAMPLES          top
```
        # tc qdisc add dev eth0 root codel
        # tc -s qdisc show
          qdisc codel 801b: dev eth0 root refcnt 2 limit 1000p target
       5.0ms interval 100.0ms
           Sent 245801662 bytes 275853 pkt (dropped 0, overlimits 0
       requeues 24)
           backlog 0b 0p requeues 24
            count 0 lastcount 0 ldelay 2us drop_next 0us
            maxpacket 7306 ecn_mark 0 drop_overlimit 0
        # tc qdisc add dev eth0 root codel limit 100 target 4ms interval
       30ms ecn
        # tc -s qdisc show
          qdisc codel 801c: dev eth0 root refcnt 2 limit 100p target
       4.0ms interval 30.0ms ecn
           Sent 237573074 bytes 268561 pkt (dropped 0, overlimits 0
       requeues 5)
           backlog 0b 0p requeues 5
            count 0 lastcount 0 ldelay 76us drop_next 0us
            maxpacket 2962 ecn_mark 0 drop_overlimit 0
```
SEE ALSO          top
```
tc(8), tc-red(8)
```
SOURCES          top
```
       Kathleen Nichols and Van Jacobson, "Controlling Queue Delay", ACM
       Queue, http://queue.acm.org/detail.cfm?id=2209336
```
AUTHORS          top
```
       CoDel was implemented by Eric Dumazet and David Taht. This manpage
       was written by Vijay Subramanian. Please reports corrections to
       the Linux Networking mailing list <netdev@vger.kernel.org>.
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
iproute2                       23 May 2012                       CoDel(8)
```
Pages that refer to this page:
    ovs-vswitchd.conf.db(5),
    tc(8),
    tc-cake(8),
    tc-fq_codel(8),
    tc-pie(8)
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

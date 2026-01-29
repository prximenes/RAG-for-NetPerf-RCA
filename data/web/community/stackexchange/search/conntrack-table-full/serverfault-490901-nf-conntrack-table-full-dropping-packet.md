---
            {
  "source": "stackexchange",
  "license": "CC BY-SA 4.0 (Stack Exchange)",
  "site": "serverfault",
  "question_id": 490901,
  "link": "https://serverfault.com/questions/490901/nf-conntrack-table-full-dropping-packet",
  "score": 3,
  "views": 11586,
  "answer_id": 490947,
  "answer_kind": "accepted",
  "tags": [
    "linux",
    "iptables",
    "firewall",
    "sysctl",
    "conntrack"
  ],
  "query_label": "conntrack-table-full",
  "description": "Conntrack exhaustion behavior and tuning (scenario_24)",
  "collected_at": "2025-12-13T16:07:14.829839+00:00"
}
            ---
            # nf_conntrack: table full, dropping packet

            ## Question
            ```
```
Mar 24 03:29:26 kernel: [1557411.243821] TCP: time wait bucket table overflow (CT0)
Mar 24 03:29:26 kernel: [1557411.243828] TCP: time wait bucket table overflow (CT0)
Mar 24 03:29:26 kernel: [1557411.243998] TCP: time wait bucket table overflow (CT0)
Mar 24 03:29:26 kernel: [1557411.244877] TCP: time wait bucket table overflow (CT0)
: [1564292.095620] __ratelimit: 37822 callbacks suppressed
Mar 24 05:24:18 kernel: [1564292.095623] nf_conntrack: table full, dropping packet.
Mar 24 05:24:18 kernel: [1564292.095629] nf_conntrack: table full, dropping packet.
Mar 24 05:24:18 kernel: [1564292.095866] nf_conntrack: table full, dropping packet.
Mar 24 05:24:18 kernel: [1564292.096156] nf_conntrack: table full, dropping packet.
Mar 24 05:24:18 kernel: [1564292.096201] nf_conntrack: table full, dropping packet.
Mar 24 05:24:18 kernel: [1564292.096232] nf_conntrack: table full, dropping packet.
Mar 24 05:24:18  kernel: [1564292.096271] nf_conntrack: table full, dropping packet.
Mar 24 05:24:18 kernel: [1564292.096310] nf_conntrack: table full, dropping packet.
Mar 24 05:24:18 kernel: [1564292.096348] nf_conntrack: table full, dropping packet.
Mar 24 05:24:18 kernel: [1564292.096376] nf_conntrack: table full, dropping packet.
```
```
-
```
```
sysctl -p
error: "net.ipv4.ip_conntrack_max" is an unknown key
error: "net.ipv4.netfilter.ip_conntrack_generic_timeout" is an unknown key
error: "net.ipv4.netfilter.ip_conntrack_icmp_timeout" is an unknown key
error: "net.ipv4.netfilter.ip_conntrack_udp_timeout_stream" is an unknown key
error: "net.ipv4.netfilter.ip_conntrack_udp_timeout" is an unknown key
error: "net.ipv4.netfilter.ip_conntrack_tcp_timeout_close" is an unknown key
error: "net.ipv4.netfilter.ip_conntrack_tcp_timeout_time_wait" is an unknown key
error: "net.ipv4.netfilter.ip_conntrack_tcp_timeout_last_ack" is an unknown key
error: "net.ipv4.netfilter.ip_conntrack_tcp_timeout_close_wait" is an unknown key
error: "net.ipv4.netfilter.ip_conntrack_tcp_timeout_fin_wait" is an unknown key
error: "net.ipv4.netfilter.ip_conntrack_tcp_timeout_established" is an unknown key
error: "net.ipv4.netfilter.ip_conntrack_tcp_timeout_syn_recv" is an unknown key
error: "net.ipv4.netfilter.ip_conntrack_tcp_timeout_syn_sent" is an unknown key
error: "net.ipv4.netfilter.ip_conntrack_max" is an unknown key
error: "net.ip_conntrack_max" is an unknown key
```
```
and
```
```
/sbin/lsmod | egrep 'ip_tables|conntrack'
xt_conntrack            3968  0
nf_conntrack_ftp       12929  1 nf_nat_ftp
nf_conntrack_ipv4       9946  55 iptable_nat,nf_nat
nf_defrag_ipv4          1531  1 nf_conntrack_ipv4
ip_tables              18151  3 iptable_filter,iptable_nat,iptable_mangle
nf_conntrack_ipv6       8732  24
nf_defrag_ipv6         12315  1 nf_conntrack_ipv6
nf_conntrack           80236  9 nf_nat_ftp,xt_conntrack,nf_conntrack_ftp,xt_connlimit,iptable_nat,nf_nat,nf_conntrack_ipv4,nf_conntrack_ipv6,xt_state
ipv6                  325405  35 ip6t_REJECT,nf_conntrack_ipv6,nf_defrag_ipv6
```
```
-
kernel
```
```
2.6.32-379.22.1.lve1.2.13.el6.x86_64 #1 SMP Fri Mar 1 09:43:47 EST 2013 x86_64 x86_64 x86_64 GNU/Linux
```
```
So what do I need to do to fix the following errors?

            ## Accepted Answer
            You are going right way. In modern kernels this parameter is called "nf_conntrack_max". Check Guntis's link at pc-freak.net , it would be useful for you.

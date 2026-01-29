---
            {
  "source": "stackexchange",
  "license": "CC BY-SA 4.0 (Stack Exchange)",
  "site": "serverfault",
  "question_id": 776218,
  "link": "https://serverfault.com/questions/776218/linux-server-failing-to-send-syn-ack-after-receiving-syn-remotely-works-locally",
  "score": 0,
  "views": 3848,
  "answer_id": 776641,
  "tags": [
    "linux",
    "iptables",
    "linux-networking",
    "tcp",
    "tcpdump"
  ],
  "query_label": "tcp-listen-synack-troubleshooting",
  "description": "SYN/SYN-ACK behavior troubleshooting; supports listen queue / SYN backlog and drops scenarios",
  "collected_at": "2025-12-13T15:57:34.591744+00:00"
}
            ---
            # Linux server failing to send SYN/ACK after receiving SYN remotely, works locally

            ## Question
            Problem:
A server process can be accessed by a device on the LAN or by the server itself, but it cannot be accessed outside the LAN (port forwarding is configured correctly as the server does receive packets).
Packet tracing reveals that SYN is received but SYN/ACK is never sent back for remote connections, but it is sent back for LAN connections.
It is worth mentioning that an SSH server is run as well; this can be connected to from both locally and remotely, so I don't quite understand what is happening with the port 5555 process.
I have spent an embarrassing amount of time trying to solve this, any feedback would be greatly appreciated!
Thank you in advance for looking through this, I know it is a wall of text.
Details:
Please note: some of the values below (such as IP addresses) have been changed for privacy reasons.
I have a process listening on port 5555 on all interfaces.
```
```
# netstat -l
Proto Recv-Q Send-Q Local Address     Foreign Address     State
tcp        0      0 *:5555            *:*                 LISTEN
...snip...
```
```
I also have a OpenVPN client connected and all internet traffic is being forwarded over it. This is a requisite and cannot be turned off except for debugging.
```
```
# ip route list
0.0.0.0/1 via 10.1.1.123 dev tun0
default via 192.168.0.1 dev enp0s14 onlink
10.1.0.1 via 10.1.1.123 dev tun0
10.1.1.123 dev tun0  proto kernel  scope link  src 10.1.1.10
94.102.56.181 via 192.168.0.1 dev enp0s14
128.0.0.0/1 via 10.1.1.123 dev tun0
192.168.0.0/24 dev enp0s14  proto kernel  scope link  src 192.168.0.101
```
```
```
iptables
```
 is configured to allow internet traffic only through the VPN. LAN traffic is permitted, and certain services are allowed such as SSH and my server process (port 5555). All else is dropped.
```
```
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT DROP
...snip...
iptables -A INPUT  -j ACCEPT -s 192.168.0.0/24 -i enp0s14
iptables -A OUTPUT -j ACCEPT -d 192.168.0.0/24 -o enp0s14
...snip...
iptables -A INPUT  -j ACCEPT -p tcp -d 192.168.0.0/24 --dport 5555 -i enp0s14
iptables -A OUTPUT -j ACCEPT -p tcp -s 192.168.0.0/24 --sport 5555 -o enp0s14
...snip...
```
```
When I run
```
tcptrack
```
 I can see my remote connection coming in.
```
```
# tcptrack -d -i enp0s14
Client                Server                State        Idle A Speed
123.123.123.123:53250 192.168.0.101:5555    SYN_SENT     32s    0 B/s
```
```
Running
```
tcpdump
```
 shows SYN is received but never sent.
```
```
# tcpdump -i enp0s14 port 5555 -vv -n
tcpdump: listening on enp0s14, link-type EN10MB (Ethernet), capture size 262144 bytes
15:46:40.375191 IP (tos 0x0, ttl 48, id 31281, offset 0, flags [DF], proto TCP (6), length 60)
    123.123.123.123.42901 > 192.168.0.101.5555: Flags [S], cksum 0x2e65 (correct), seq 808682189, win 14600, options [mss 1460,sackOK,TS val 3488166776 ecr 0,nop,wscale 7], length 0
15:46:47.235302 IP (tos 0x0, ttl 48, id 3275, offset 0, flags [DF], proto TCP (6), length 60)
    123.123.123.123.41151 > 192.168.0.101.5555: Flags [S], cksum 0xa8d0 (correct), seq 2596314499, win 14600, options [mss 1460,sackOK,TS val 1660719432 ecr 0,nop,wscale 7], length 0
15:46:48.234346 IP (tos 0x0, ttl 48, id 3276, offset 0, flags [DF], proto TCP (6), length 60)
    123.123.123.123.41151 > 192.168.0.101.5555: Flags [S], cksum 0xa4e8 (correct), seq 2596314499, win 14600, options [mss 1460,sackOK,TS val 1660720432 ecr 0,nop,wscale 7], length 0
...snip...
```
```
A really curious thing is that inspecting the packet count of
```
iptables
```
 rules shows both the INPUT and OUTPUT chains accepting the outside connection just fine as the packet count increases.
```
```
# iptables -vxnL | grep 5555
 99     5940 ACCEPT     tcp  --  enp0s14 *       0.0.0.0/0            192.168.0.0/24       tcp dpt:5555
235    11980 ACCEPT     tcp  --  *      enp0s14  192.168.0.0/24       0.0.0.0/0            tcp spt:5555
...connection attempt...
# iptables -vxnL | grep 5555
103     6180 ACCEPT     tcp  --  enp0s14 *       0.0.0.0/0            192.168.0.0/24       tcp dpt:5555
239    12184 ACCEPT     tcp  --  *      enp0s14  192.168.0.0/24       0.0.0.0/0            tcp spt:5555
```
```
Here are my
```
sysctl
```
 variables in the event they are of any help:
```
```
# sysctl -a | grep "net\.\(core\|ipv4\)"
net.core.bpf_jit_enable = 0
net.core.busy_poll = 0
net.core.busy_read = 0
net.core.default_qdisc = pfifo_fast
net.core.dev_weight = 64
net.core.flow_limit_cpu_bitmap = 0
net.core.flow_limit_table_len = 4096
net.core.max_skb_frags = 17
net.core.message_burst = 10
net.core.message_cost = 5
net.core.netdev_budget = 300
net.core.netdev_max_backlog = 65536
net.core.netdev_tstamp_prequeue = 1
net.core.optmem_max = 25165824
net.core.rmem_default = 16777216
net.core.rmem_max = 16777216
net.core.rps_sock_flow_entries = 0
net.core.somaxconn = 4096
net.core.tstamp_allow_data = 1
net.core.warnings = 0
net.core.wmem_default = 16777216
net.core.wmem_max = 16777216
net.core.xfrm_acq_expires = 30
net.core.xfrm_aevent_etime = 10
net.core.xfrm_aevent_rseqth = 2
net.core.xfrm_larval_drop = 1
net.ipv4.cipso_cache_bucket_size = 10
net.ipv4.cipso_cache_enable = 1
net.ipv4.cipso_rbm_optfmt = 0
net.ipv4.cipso_rbm_strictvalid = 1
net.ipv4.conf.all.accept_local = 0
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.all.accept_source_route = 0
net.ipv4.conf.all.arp_accept = 0
net.ipv4.conf.all.arp_announce = 0
net.ipv4.conf.all.arp_filter = 0
net.ipv4.conf.all.arp_ignore = 0
net.ipv4.conf.all.arp_notify = 0
net.ipv4.conf.all.bootp_relay = 0
net.ipv4.conf.all.disable_policy = 0
net.ipv4.conf.all.disable_xfrm = 0
net.ipv4.conf.all.force_igmp_version = 0
net.ipv4.conf.all.forwarding = 0
net.ipv4.conf.all.igmpv2_unsolicited_report_interval = 10000
net.ipv4.conf.all.igmpv3_unsolicited_report_interval = 1000
net.ipv4.conf.all.ignore_routes_with_linkdown = 0
net.ipv4.conf.all.log_martians = 0
net.ipv4.conf.all.mc_forwarding = 0
net.ipv4.conf.all.medium_id = 0
net.ipv4.conf.all.promote_secondaries = 0
net.ipv4.conf.all.proxy_arp = 0
net.ipv4.conf.all.proxy_arp_pvlan = 0
net.ipv4.conf.all.route_localnet = 0
net.ipv4.conf.all.rp_filter = 1
net.ipv4.conf.all.secure_redirects = 1
net.ipv4.conf.all.send_redirects = 0
net.ipv4.conf.all.shared_media = 1
net.ipv4.conf.all.src_valid_mark = 0
net.ipv4.conf.all.tag = 0
net.ipv4.conf.default.accept_local = 0
net.ipv4.conf.default.accept_redirects = 1
net.ipv4.conf.default.accept_source_route = 1
net.ipv4.conf.default.arp_accept = 0
net.ipv4.conf.default.arp_announce = 0
net.ipv4.conf.default.arp_filter = 0
net.ipv4.conf.default.arp_ignore = 0
net.ipv4.conf.default.arp_notify = 0
net.ipv4.conf.default.bootp_relay = 0
net.ipv4.conf.default.disable_policy = 0
net.ipv4.conf.default.disable_xfrm = 0
net.ipv4.conf.default.force_igmp_version = 0
net.ipv4.conf.default.forwarding = 0
net.ipv4.conf.default.igmpv2_unsolicited_report_interval = 10000
net.ipv4.conf.default.igmpv3_unsolicited_report_interval = 1000
net.ipv4.conf.default.ignore_routes_with_linkdown = 0
net.ipv4.conf.default.log_martians = 0
net.ipv4.conf.default.mc_forwarding = 0
net.ipv4.conf.default.medium_id = 0
net.ipv4.conf.default.promote_secondaries = 0
net.ipv4.conf.default.proxy_arp = 0
net.ipv4.conf.default.proxy_arp_pvlan = 0
net.ipv4.conf.default.route_localnet = 0
net.ipv4.conf.default.rp_filter = 1
net.ipv4.conf.default.secure_redirects = 1
net.ipv4.conf.default.send_redirects = 1
net.ipv4.conf.default.shared_media = 1
net.ipv4.conf.default.src_valid_mark = 0
net.ipv4.conf.default.tag = 0
net.ipv4.conf.enp0s14.accept_local = 0
net.ipv4.conf.enp0s14.accept_redirects = 1
net.ipv4.conf.enp0s14.accept_source_route = 1
net.ipv4.conf.enp0s14.arp_accept = 0
net.ipv4.conf.enp0s14.arp_announce = 0
net.ipv4.conf.enp0s14.arp_filter = 0
net.ipv4.conf.enp0s14.arp_ignore = 0
net.ipv4.conf.enp0s14.arp_notify = 0
net.ipv4.conf.enp0s14.bootp_relay = 0
net.ipv4.conf.enp0s14.disable_policy = 0
net.ipv4.conf.enp0s14.disable_xfrm = 0
net.ipv4.conf.enp0s14.force_igmp_version = 0
net.ipv4.conf.enp0s14.forwarding = 0
net.ipv4.conf.enp0s14.igmpv2_unsolicited_report_interval = 10000
net.ipv4.conf.enp0s14.igmpv3_unsolicited_report_interval = 1000
net.ipv4.conf.enp0s14.ignore_routes_with_linkdown = 0
net.ipv4.conf.enp0s14.log_martians = 0
net.ipv4.conf.enp0s14.mc_forwarding = 0
net.ipv4.conf.enp0s14.medium_id = 0
net.ipv4.conf.enp0s14.promote_secondaries = 0
net.ipv4.conf.enp0s14.proxy_arp = 0
net.ipv4.conf.enp0s14.proxy_arp_pvlan = 0
net.ipv4.conf.enp0s14.route_localnet = 0
net.ipv4.conf.enp0s14.rp_filter = 1
net.ipv4.conf.enp0s14.secure_redirects = 1
net.ipv4.conf.enp0s14.send_redirects = 1
net.ipv4.conf.enp0s14.shared_media = 1
net.ipv4.conf.enp0s14.src_valid_mark = 0
net.ipv4.conf.enp0s14.tag = 0
net.ipv4.conf.lo.accept_local = 0
net.ipv4.conf.lo.accept_redirects = 1
net.ipv4.conf.lo.accept_source_route = 1
net.ipv4.conf.lo.arp_accept = 0
net.ipv4.conf.lo.arp_announce = 0
net.ipv4.conf.lo.arp_filter = 0
net.ipv4.conf.lo.arp_ignore = 0
net.ipv4.conf.lo.arp_notify = 0
net.ipv4.conf.lo.bootp_relay = 0
net.ipv4.conf.lo.disable_policy = 1
net.ipv4.conf.lo.disable_xfrm = 1
net.ipv4.conf.lo.force_igmp_version = 0
net.ipv4.conf.lo.forwarding = 0
net.ipv4.conf.lo.igmpv2_unsolicited_report_interval = 10000
net.ipv4.conf.lo.igmpv3_unsolicited_report_interval = 1000
net.ipv4.conf.lo.ignore_routes_with_linkdown = 0
net.ipv4.conf.lo.log_martians = 0
net.ipv4.conf.lo.mc_forwarding = 0
net.ipv4.conf.lo.medium_id = 0
net.ipv4.conf.lo.promote_secondaries = 0
net.ipv4.conf.lo.proxy_arp = 0
net.ipv4.conf.lo.proxy_arp_pvlan = 0
net.ipv4.conf.lo.route_localnet = 0
net.ipv4.conf.lo.rp_filter = 0
net.ipv4.conf.lo.secure_redirects = 1
net.ipv4.conf.lo.send_redirects = 1
net.ipv4.conf.lo.shared_media = 1
net.ipv4.conf.lo.src_valid_mark = 0
net.ipv4.conf.lo.tag = 0
net.ipv4.conf.tun0.accept_local = 0
net.ipv4.conf.tun0.accept_redirects = 1
net.ipv4.conf.tun0.accept_source_route = 1
net.ipv4.conf.tun0.arp_accept = 0
net.ipv4.conf.tun0.arp_announce = 0
net.ipv4.conf.tun0.arp_filter = 0
net.ipv4.conf.tun0.arp_ignore = 0
net.ipv4.conf.tun0.arp_notify = 0
net.ipv4.conf.tun0.bootp_relay = 0
net.ipv4.conf.tun0.disable_policy = 0
net.ipv4.conf.tun0.disable_xfrm = 0
net.ipv4.conf.tun0.force_igmp_version = 0
net.ipv4.conf.tun0.forwarding = 0
net.ipv4.conf.tun0.igmpv2_unsolicited_report_interval = 10000
net.ipv4.conf.tun0.igmpv3_unsolicited_report_interval = 1000
net.ipv4.conf.tun0.ignore_routes_with_linkdown = 0
net.ipv4.conf.tun0.log_martians = 0
net.ipv4.conf.tun0.mc_forwarding = 0
net.ipv4.conf.tun0.medium_id = 0
net.ipv4.conf.tun0.promote_secondaries = 0
net.ipv4.conf.tun0.proxy_arp = 0
net.ipv4.conf.tun0.proxy_arp_pvlan = 0
net.ipv4.conf.tun0.route_localnet = 0
net.ipv4.conf.tun0.rp_filter = 1
net.ipv4.conf.tun0.secure_redirects = 1
net.ipv4.conf.tun0.send_redirects = 1
net.ipv4.conf.tun0.shared_media = 1
net.ipv4.conf.tun0.src_valid_mark = 0
net.ipv4.conf.tun0.tag = 0
net.ipv4.fwmark_reflect = 0
net.ipv4.icmp_echo_ignore_all = 0
net.ipv4.icmp_echo_ignore_broadcasts = 1
net.ipv4.icmp_errors_use_inbound_ifaddr = 0
net.ipv4.icmp_ignore_bogus_error_responses = 1
net.ipv4.icmp_msgs_burst = 50
net.ipv4.icmp_msgs_per_sec = 1000
net.ipv4.icmp_ratelimit = 1000
net.ipv4.icmp_ratemask = 6168
net.ipv4.igmp_link_local_mcast_reports = 1
net.ipv4.igmp_max_memberships = 20
net.ipv4.igmp_max_msf = 10
net.ipv4.igmp_qrv = 2
net.ipv4.inet_peer_maxttl = 600
net.ipv4.inet_peer_minttl = 120
net.ipv4.inet_peer_threshold = 65664
net.ipv4.ip_default_ttl = 64
net.ipv4.ip_dynaddr = 0
net.ipv4.ip_early_demux = 1
net.ipv4.ip_forward = 0
net.ipv4.ip_forward_use_pmtu = 0
net.ipv4.ip_local_port_range = 32768    60999
net.ipv4.ip_local_reserved_ports =
net.ipv4.ip_no_pmtu_disc = 0
net.ipv4.ip_nonlocal_bind = 0
net.ipv4.ipfrag_high_thresh = 4194304
net.ipv4.ipfrag_low_thresh = 3145728
net.ipv4.ipfrag_max_dist = 64
net.ipv4.ipfrag_secret_interval = 0
net.ipv4.ipfrag_time = 30
net.ipv4.neigh.default.anycast_delay = 100
net.ipv4.neigh.default.app_solicit = 0
net.ipv4.neigh.default.base_reachable_time_ms = 30000
net.ipv4.neigh.default.delay_first_probe_time = 5
net.ipv4.neigh.default.gc_interval = 30
net.ipv4.neigh.default.gc_stale_time = 60
net.ipv4.neigh.default.gc_thresh1 = 128
net.ipv4.neigh.default.gc_thresh2 = 512
net.ipv4.neigh.default.gc_thresh3 = 1024
net.ipv4.neigh.default.locktime = 100
net.ipv4.neigh.default.mcast_resolicit = 0
net.ipv4.neigh.default.mcast_solicit = 3
net.ipv4.neigh.default.proxy_delay = 80
net.ipv4.neigh.default.proxy_qlen = 64
net.ipv4.neigh.default.retrans_time_ms = 1000
net.ipv4.neigh.default.ucast_solicit = 3
net.ipv4.neigh.default.unres_qlen = 31
net.ipv4.neigh.default.unres_qlen_bytes = 65536
net.ipv4.neigh.enp0s14.anycast_delay = 100
net.ipv4.neigh.enp0s14.app_solicit = 0
net.ipv4.neigh.enp0s14.base_reachable_time_ms = 30000
net.ipv4.neigh.enp0s14.delay_first_probe_time = 5
net.ipv4.neigh.enp0s14.gc_stale_time = 60
net.ipv4.neigh.enp0s14.locktime = 100
net.ipv4.neigh.enp0s14.mcast_resolicit = 0
net.ipv4.neigh.enp0s14.mcast_solicit = 3
net.ipv4.neigh.enp0s14.proxy_delay = 80
net.ipv4.neigh.enp0s14.proxy_qlen = 64
net.ipv4.neigh.enp0s14.retrans_time_ms = 1000
net.ipv4.neigh.enp0s14.ucast_solicit = 3
net.ipv4.neigh.enp0s14.unres_qlen = 31
net.ipv4.neigh.enp0s14.unres_qlen_bytes = 65536
net.ipv4.neigh.lo.anycast_delay = 100
net.ipv4.neigh.lo.app_solicit = 0
net.ipv4.neigh.lo.base_reachable_time_ms = 30000
net.ipv4.neigh.lo.delay_first_probe_time = 5
net.ipv4.neigh.lo.gc_stale_time = 60
net.ipv4.neigh.lo.locktime = 100
net.ipv4.neigh.lo.mcast_resolicit = 0
net.ipv4.neigh.lo.mcast_solicit = 3
net.ipv4.neigh.lo.proxy_delay = 80
net.ipv4.neigh.lo.proxy_qlen = 64
net.ipv4.neigh.lo.retrans_time_ms = 1000
net.ipv4.neigh.lo.ucast_solicit = 3
net.ipv4.neigh.lo.unres_qlen = 31
net.ipv4.neigh.lo.unres_qlen_bytes = 65536
net.ipv4.neigh.tun0.anycast_delay = 100
net.ipv4.neigh.tun0.app_solicit = 0
net.ipv4.neigh.tun0.base_reachable_time_ms = 30000
net.ipv4.neigh.tun0.delay_first_probe_time = 5
net.ipv4.neigh.tun0.gc_stale_time = 60
net.ipv4.neigh.tun0.locktime = 100
net.ipv4.neigh.tun0.mcast_resolicit = 0
net.ipv4.neigh.tun0.mcast_solicit = 3
net.ipv4.neigh.tun0.proxy_delay = 80
net.ipv4.neigh.tun0.proxy_qlen = 64
net.ipv4.neigh.tun0.retrans_time_ms = 1000
net.ipv4.neigh.tun0.ucast_solicit = 3
net.ipv4.neigh.tun0.unres_qlen = 31
net.ipv4.neigh.tun0.unres_qlen_bytes = 65536
net.ipv4.ping_group_range = 1   0
net.ipv4.route.error_burst = 1250
net.ipv4.route.error_cost = 250
net.ipv4.route.gc_elasticity = 8
net.ipv4.route.gc_interval = 60
net.ipv4.route.gc_min_interval = 0
net.ipv4.route.gc_min_interval_ms = 500
net.ipv4.route.gc_thresh = -1
net.ipv4.route.gc_timeout = 300
net.ipv4.route.max_size = 2147483647
net.ipv4.route.min_adv_mss = 256
net.ipv4.route.min_pmtu = 552
net.ipv4.route.mtu_expires = 600
net.ipv4.route.redirect_load = 5
net.ipv4.route.redirect_number = 9
net.ipv4.route.redirect_silence = 5120
net.ipv4.tcp_abort_on_overflow = 0
net.ipv4.tcp_adv_win_scale = 1
net.ipv4.tcp_allowed_congestion_control = cubic reno
net.ipv4.tcp_app_win = 31
net.ipv4.tcp_autocorking = 1
net.ipv4.tcp_available_congestion_control = cubic reno
net.ipv4.tcp_base_mss = 1024
net.ipv4.tcp_challenge_ack_limit = 100
net.ipv4.tcp_congestion_control = cubic
net.ipv4.tcp_dsack = 1
net.ipv4.tcp_early_retrans = 3
net.ipv4.tcp_ecn = 2
net.ipv4.tcp_ecn_fallback = 1
net.ipv4.tcp_fack = 1
net.ipv4.tcp_fastopen = 1
net.ipv4.tcp_fastopen_key = 00000000-00000000-00000000-00000000
net.ipv4.tcp_fin_timeout = 15
net.ipv4.tcp_frto = 2
net.ipv4.tcp_fwmark_accept = 0
net.ipv4.tcp_invalid_ratelimit = 500
net.ipv4.tcp_keepalive_intvl = 15
net.ipv4.tcp_keepalive_probes = 5
net.ipv4.tcp_keepalive_time = 300
net.ipv4.tcp_limit_output_bytes = 262144
net.ipv4.tcp_low_latency = 0
net.ipv4.tcp_max_orphans = 32768
net.ipv4.tcp_max_reordering = 300
net.ipv4.tcp_max_syn_backlog = 256
net.ipv4.tcp_max_tw_buckets = 32768
net.ipv4.tcp_mem = 65536        131072  262144
net.ipv4.tcp_min_rtt_wlen = 300
net.ipv4.tcp_min_tso_segs = 2
net.ipv4.tcp_moderate_rcvbuf = 1
net.ipv4.tcp_mtu_probing = 0
net.ipv4.tcp_no_metrics_save = 0
net.ipv4.tcp_notsent_lowat = -1
net.ipv4.tcp_orphan_retries = 0
net.ipv4.tcp_pacing_ca_ratio = 120
net.ipv4.tcp_pacing_ss_ratio = 200
net.ipv4.tcp_probe_interval = 600
net.ipv4.tcp_probe_threshold = 8
net.ipv4.tcp_recovery = 1
net.ipv4.tcp_reordering = 3
net.ipv4.tcp_retrans_collapse = 1
net.ipv4.tcp_retries1 = 3
net.ipv4.tcp_retries2 = 15
net.ipv4.tcp_rfc1337 = 0
net.ipv4.tcp_rmem = 4096        524288  16777216
net.ipv4.tcp_sack = 1
net.ipv4.tcp_slow_start_after_idle = 1
net.ipv4.tcp_stdurg = 0
net.ipv4.tcp_syn_retries = 6
net.ipv4.tcp_synack_retries = 5
net.ipv4.tcp_syncookies = 0
net.ipv4.tcp_thin_dupack = 0
net.ipv4.tcp_thin_linear_timeouts = 0
net.ipv4.tcp_timestamps = 0
net.ipv4.tcp_tso_win_divisor = 3
net.ipv4.tcp_tw_recycle = 0
net.ipv4.tcp_tw_reuse = 0
net.ipv4.tcp_window_scaling = 0
net.ipv4.tcp_wmem = 4096        524288  16777216
net.ipv4.tcp_workaround_signed_windows = 0
net.ipv4.udp_mem = 65536        131072  262144
net.ipv4.udp_rmem_min = 4096
net.ipv4.udp_wmem_min = 4096
net.ipv4.xfrm4_gc_thresh = 2147483647
```
```
I have tried doing a few things per these Server Fault answers:
Why would a server not send a SYN/ACK packet in response to a SYN packet
- Setting both
```
net.ipv4.tcp_timestamps
```
 and
```
net.ipv4.tcp_window_scaling
```
 to
```
0
```
Dropping of connections with tcp_tw_recycle
- A mix of setting
```
net.ipv4.tcp_tw_reuse
```
 and
```
net.ipv4.tcp_tw_recycle
```
 to
```
0
```
However, neither of those do anything to fix the issue.
I have a feeling like the VPN might be getting in the way somehow, but even with the VPN disabled I cannot access the process from outside the network.
Any thoughts would be greatly appreciated!

            ## Accepted Answer
            I found the solution myself thanks in part to @symcbean's comment which got me thinking.
It turns out, that for whatever reason, Linux does not route response packets back on the interface they connected on. To fix this we set up advanced routing.
```
```
ip rule add fwmark 1 table mycustomtable
ip route add table mycustomtable 0.0.0.0/0 via 192.168.0.1 dev enp0s14
```
```
I then use an
```
iptables
```
 rule to mark the packets:
```
```
iptables -t mangle -A OUTPUT -j MARK --set-mark 1 -s 192.168.0.0/24 -p tcp --sport 5555
```
```
The confusing (and annoying) part is that none of this works unless you set the
```
rp_filter
```
 sysctl variable to something less restrictive. I'm using '2' but you can also use '0'.
```
```
sysctl -w net.ipv4.conf.enp0s14.rp_filter=2
```
```
Hope this helps someone out there in the same boat.

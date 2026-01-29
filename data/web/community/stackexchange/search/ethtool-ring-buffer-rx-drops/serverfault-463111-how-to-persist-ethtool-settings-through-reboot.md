---
            {
  "source": "stackexchange",
  "license": "CC BY-SA 4.0 (Stack Exchange)",
  "site": "serverfault",
  "question_id": 463111,
  "link": "https://serverfault.com/questions/463111/how-to-persist-ethtool-settings-through-reboot",
  "score": 28,
  "views": 69316,
  "answer_id": 463112,
  "answer_kind": "accepted",
  "tags": [
    "centos",
    "linux-networking",
    "ethtool"
  ],
  "query_label": "ethtool-ring-buffer-rx-drops",
  "description": "NIC ring buffer tuning / rx_dropped (scenario_06)",
  "collected_at": "2025-12-13T16:07:07.342973+00:00"
}
            ---
            # How to persist ethtool settings through reboot

            ## Question
            I would like to turn off tcp segmentation offload on a CentOS5 server. Using ethtool the command is
```
ethtool -K eth0 tso off
```
 However, this setting only persists for this session. How can I make it persist through reboots?

            ## Accepted Answer
            From this webpage:
You can enter the ethtool commands in
```
/etc/rc.local
```
 (or your distribution's equivalent) where commands are run after the current runlevel completes, but this isn't ideal. Network services may have started during the runlevel and ethtool commands tend to interrupt network traffic. It would be more preferable to have the commands applied as the interface is brought up.
The network service in CentOS has the ability to do this. The script
```
/etc/sysconfig/network-scripts/ifup-post
```
 checks for the existence of
```
/sbin/ifup-local
```
, and if it exists, runs it with the interface name as a parameter (eg:
```
/sbin/ifup-local eth0
```
)
We can create this file with touch
```
/sbin/ifup-local
```
 make it executable with
```
chmod +x /sbin/ifup-local
```
 set its SELinux context with
```
chcon --reference /sbin/ifup /sbin/ifup-local
```
 and then open it in an editor.
A simple script to apply the same settings to all interfaces would be something like
```
```
#!/bin/bash
if [ -n "$1" ]; then
/sbin/ethtool -G $1 rx 4096 tx 4096
/sbin/ethtool -K $1 tso on gso on
fi
```
```
Keep in mind this will attempt to apply settings to ALL interfaces, even the loopback.
If we have different interfaces we want to apply different settings to, or want to skip the loopback, we can make a case statement
```
```
#!/bin/bash
case "$1" in
eth0)
/sbin/ethtool -G $1 rx 16384 tx 16384
/sbin/ethtool -K $1 gso on gro on
;;
eth1)
/sbin/ethtool -G $1 rx 64 tx 64
/sbin/ethtool -K $1 tso on gso on
/sbin/ip link set $1 txqueuelen 0
;;
esac
exit 0
```
```
Now ethtool settings are applied to interfaces as they start, all potential interruptions to network communication are done as the interface is brought up, and your server can continue to boot with full network capabilities.

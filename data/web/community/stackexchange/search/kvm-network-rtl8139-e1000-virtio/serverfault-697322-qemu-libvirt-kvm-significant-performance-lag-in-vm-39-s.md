---
            {
  "source": "stackexchange",
  "license": "CC BY-SA 4.0 (Stack Exchange)",
  "site": "serverfault",
  "question_id": 697322,
  "link": "https://serverfault.com/questions/697322/qemulibvirtkvm-significant-performance-lag-in-vms",
  "score": 3,
  "views": 5597,
  "answer_id": 765791,
  "answer_kind": "accepted",
  "tags": [
    "performance",
    "virtual-machines",
    "kvm-virtualization",
    "libvirt",
    "qemu"
  ],
  "query_label": "kvm-network-rtl8139-e1000-virtio",
  "description": "KVM NIC model performance issues (scenarios_08-13)",
  "collected_at": "2025-12-13T16:07:11.075540+00:00"
}
            ---
            # Qemu+libvirt+kvm significant performance lag in VM&#39;s

            ## Question
            I am troubleshooting poor performance on our new VM host machine which is a Dell PowerEdge R415 with hardware RAID.
We've got about 20 VM's running like this:
```
```
qemu-system-x86_64 \
  -enable-kvm \
  -name rc.stb.mezzanine -S \
  -machine pc-0.12,accel=kvm,usb=off \
  -m 2048 \
  -realtime mlock=off \
  -smp 2,sockets=2,cores=1,threads=1 \
  -uuid 493d519c-8bb5-2cf8-c037-1094a3c48a7a \
  -no-user-config \
  -nodefaults \
  -chardev socket,id=charmonitor,path=/var/lib/libvirt/qemu/rc.stb.monitor,server,nowait \
  -mon chardev=charmonitor,id=monitor,mode=control \
  -rtc base=utc \
  -no-shutdown \
  -boot strict=on \
  -device piix3-usb-uhci,id=usb,bus=pci.0,addr=0x1.0x2 \
  -drive file=/dev/vg-raid/lv-rc,if=none,id=drive-virtio-disk0,format=raw \
  -device virtio-blk-pci,scsi=off,bus=pci.0,addr=0x5,drive=drive-virtio-disk0,id=virtio-disk0,bootindex=1 \
  -drive file=/var/lib/libvirt/images/ubuntu-14.04-server-amd64.iso,if=none,id=drive-ide0-1-0,readonly=on,format=raw \
  -device ide-cd,bus=ide.1,unit=0,drive=drive-ide0-1-0,id=ide0-1-0,bootindex=2 \
  -netdev tap,fd=32,id=hostnet0 \
  -device e1000,netdev=hostnet0,id=net0,mac=52:54:df:26:15:e9,bus=pci.0,addr=0x3 \
  -chardev pty,id=charserial0 \
  -device isa-serial,chardev=charserial0,id=serial0 \
  -vnc 127.0.0.1:1 -device cirrus-vga,id=video0,bus=pci.0,addr=0x2 \
  -device ES1370,id=sound0,bus=pci.0,addr=0x4 \
  -device virtio-balloon-pci,id=balloon0,bus=pci.0,addr=0x6
```
```
The VM host uses a completely stock Ubuntu 14.04 LTS setup with a bridge interface in front of libvirt+qemu.
The problem is basically that the VM's are experiencing sporadic "lag". It's experienced as serious performance issues by the users.  Sometimes it's hardly noticable, yet sometimes a single VM can struggle to respond to ping in time as shown below (tested from the VM Host to eliminate any network related issues).
```
```
root@vm-host-1:~# ping rc
PING rc (192.168.200.7) 56(84) bytes of data.
64 bytes from rc (192.168.200.7): icmp_seq=1 ttl=64 time=0.202 ms
64 bytes from rc (192.168.200.7): icmp_seq=2 ttl=64 time=0.214 ms
64 bytes from rc (192.168.200.7): icmp_seq=3 ttl=64 time=0.241 ms
64 bytes from rc (192.168.200.7): icmp_seq=4 ttl=64 time=0.276 ms
64 bytes from rc (192.168.200.7): icmp_seq=5 ttl=64 time=0.249 ms
64 bytes from rc (192.168.200.7): icmp_seq=6 ttl=64 time=0.228 ms
64 bytes from rc (192.168.200.7): icmp_seq=7 ttl=64 time=0.198 ms
64 bytes from rc (192.168.200.7): icmp_seq=8 ttl=64 time=3207 ms
64 bytes from rc (192.168.200.7): icmp_seq=9 ttl=64 time=2207 ms
64 bytes from rc (192.168.200.7): icmp_seq=10 ttl=64 time=1203 ms
64 bytes from rc (192.168.200.7): icmp_seq=11 ttl=64 time=203 ms
64 bytes from rc (192.168.200.7): icmp_seq=12 ttl=64 time=0.240 ms
64 bytes from rc (192.168.200.7): icmp_seq=13 ttl=64 time=0.271 ms
64 bytes from rc (192.168.200.7): icmp_seq=14 ttl=64 time=0.279 ms
^C
--- rc.mezzanine ping statistics ---
14 packets transmitted, 14 received, 0% packet loss, time 13007ms
rtt min/avg/max/mdev = 0.198/487.488/3207.376/975.558 ms, pipe 4
```
```
Local commands run on the respective VM's are also occasionally slow, e.g. running 'ls' might usually take a split second, but occasionally it takes a second or two. Clearly something is unhealthy.
I've been chasing this problem for several days.  The VM host's disks are healthy, and memory usage isn't bad, as can be seen from:
```
```
virt-top 10:24:10 - x86_64 12/12CPU 3000MHz 64401MB
20 domains, 20 active, 20 running, 0 sleeping, 0 paused, 0 inactive D:0 O:0 X:0
CPU: 0.0%  Mem: 28800 MB (28800 MB by guests)
```
```
And
```
```
root@vm-host-1:~# free -m
             total       used       free     shared    buffers     cached
Mem:         64401      57458       6943          0      32229        338
-/+ buffers/cache:      24889      39511
Swap:         7628        276       7352
```
```
This server is perfectly capable of running this amount of VM's, especially considering that they are not high load VM's - but mostly idling.
What's the procedure to troubleshoot this?   I suspect that one of the VM's is misbehaving, causing ripple effects that affect all the VM's, but I have yet to determine which VM this is, due to the sporadic occurrences of the problem.
The VM host hardware on its own is perfectly healthy - and gives no issues when run without VM's, so I suspect this is a qemu/libvirt/kvm issue - perhaps triggered by a misbehaving VM.
Slabtop output:
```
```
 Active / Total Objects (% used)    : 17042162 / 17322929 (98.4%)
 Active / Total Slabs (% used)      : 365122 / 365122 (100.0%)
 Active / Total Caches (% used)     : 69 / 125 (55.2%)
 Active / Total Size (% used)       : 1616671.38K / 1677331.17K (96.4%)
 Minimum / Average / Maximum Object : 0.01K / 0.10K / 14.94K
  OBJS ACTIVE  USE OBJ SIZE  SLABS OBJ/SLAB CACHE SIZE NAME
9326928 9219652  98%    0.10K 239152       39    956608K buffer_head
6821888 6821559  99%    0.06K 106592       64    426368K kmalloc-64
465375 369738  79%    0.05K   5475       85     21900K shared_policy_node
260689 230992  88%    0.55K   4577       57    146464K radix_tree_node
 65280  63353  97%    0.03K    510      128      2040K kmalloc-32
 46494  45631  98%    0.19K   1107       42      8856K dentry
 45936  23865  51%    0.96K   1392       33     44544K ext4_inode_cache
 44136  43827  99%    0.11K   1226       36      4904K sysfs_dir_cache
 29148  21588  74%    0.19K    694       42      5552K kmalloc-192
 22784  18513  81%    0.02K     89      256       356K kmalloc-16
 19890  19447  97%    0.04K    195      102       780K Acpi-Namespace
 19712  19320  98%    0.50K    616       32      9856K kmalloc-512
 16744  15338  91%    0.57K    299       56      9568K inode_cache
 16320  16015  98%    0.04K    160      102       640K ext4_extent_status
 15216  14690  96%    0.16K    317       48      2536K kvm_mmu_page_header
 12288  12288 100%    0.01K     24      512        96K kmalloc-8
 12160  11114  91%    0.06K    190       64       760K anon_vma
  7776   5722  73%    0.25K    244       32      1952K kmalloc-256
  7056   7056 100%    0.09K    168       42       672K kmalloc-96
  5920   4759  80%    0.12K    185       32       740K kmalloc-128
  5050   4757  94%    0.63K    101       50      3232K proc_inode_cache
  4940   4046  81%    0.30K     95       52      1520K nf_conntrack_ffffffff81cd9b00
  3852   3780  98%    0.11K    107       36       428K jbd2_journal_head
  3744   2911  77%    2.00K    234       16      7488K kmalloc-2048
  3696   3696 100%    0.07K     66       56       264K ext4_io_end
  3296   2975  90%    1.00K    103       32      3296K kmalloc-1024
```
```

            ## Accepted Answer
            We've plunged into the same issue.
Caused by Ubuntu 14.04 kernel bug.
Solution #1:
Update Kernel to 3.13.0-33.58 (or newer)
Solution #2:
Disable KSM

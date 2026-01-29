---
            {
  "source": "stackexchange",
  "license": "CC BY-SA 4.0 (Stack Exchange)",
  "site": "serverfault",
  "question_id": 931228,
  "link": "https://serverfault.com/questions/931228/error-in-enbling-sr-iov-with-ubuntu-18-04-on-intel-ixgbe-intel-x550-dell-r64",
  "score": 2,
  "views": 5094,
  "answer_id": 931288,
  "tags": [
    "virtualization",
    "dell-poweredge",
    "intel",
    "ubuntu-18.04",
    "sr-iov"
  ],
  "query_label": "sriov-enablement-intel-ixgbe",
  "description": "Enabling SR-IOV on Intel NICs; practical steps and pitfalls",
  "collected_at": "2025-12-13T15:57:40.303781+00:00"
}
            ---
            # Error in enbling SR-IOV with Ubuntu 18.04 on Intel ixgbe - Intel X550 - Dell R640

            ## Question
            I'm having issues on creating VF with ubuntu 18.04.
SR-IOV is enabled from BIOS, the NIC are Intel X550, I added
```
intel_iommu=on
```
 to
```
/etc/default/grub
```
 and also tried using modprobe.d
by adding
```
options ixgbe max_vfs=8
```
 on
```
/etc/modprobe.d/ixgbe.conf
```
But if I check using
```
lspci | grep -i ethernet
```
 I only get the physical cards.
I have also tried:
```
```
# echo '7' > /sys/class/net/eno1/device/sriov_numvfs
bash: /sys/class/net/eno1/device/sriov_numvfs: Permission denied
```
```
Is the configuration correct?
From dmesg I get:
```
```
$ dmesg | grep iov
[  137.321216] ixgbe 0000:19:00.0 0000:19:00.0 (uninitialized): Failed to enable PCI sriov: -38
[  138.295030] ixgbe 0000:19:00.1 0000:19:00.1 (uninitialized): Failed to enable PCI sriov: -38
[  139.263114] ixgbe 0000:1a:00.0 0000:1a:00.0 (uninitialized): Failed to enable PCI sriov: -38
[  140.227147] ixgbe 0000:1a:00.1 0000:1a:00.1 (uninitialized): Failed to enable PCI sriov: -38
```
```
If may be usedfull here you can find the dmesg | grep iommu
and the full dmesg
Many thanks.
Gabriele

            ## Accepted Answer
            I solved this, was a lack of documentation from Dell side.
I had to enable also SR-IOV for each NIC, in the Device Settigs from the System Configuration, the global enabler is not enough.

---
            {
  "source": "stackexchange",
  "license": "CC BY-SA 4.0 (Stack Exchange)",
  "site": "serverfault",
  "question_id": 520035,
  "link": "https://serverfault.com/questions/520035/linux-kvm-guest-hanging-after-several-weeks",
  "score": 4,
  "views": 4885,
  "answer_id": 534493,
  "answer_kind": "accepted",
  "tags": [
    "linux",
    "kvm-virtualization"
  ],
  "query_label": "kvm-network-rtl8139-e1000-virtio",
  "description": "KVM NIC model performance issues (scenarios_08-13)",
  "collected_at": "2025-12-13T16:07:10.648125+00:00"
}
            ---
            # Linux KVM guest hanging after several weeks

            ## Question
            I've got a Linux KVM guest that hangs after several weeks.  Looking at the virt-manager window shows 100% CPU usage.
```
virsh reboot guest
```
 doesn't take any effect, the guest needs to be forced off.  On the guest I can see no indication of what went wrong.  I've scanned /var/log/messages and just about any other log file that can might tell me something.  After rebooting the system is stable for several weeks and then hangs again.
I've tried the following things:
- Add clocksource=acpi_pm to the kernel boot options
- Changing the disk bus from Virtio to IDE
- Changing the NIC to e1000
All to no avail.  Right now I'm at a point where I reboot the server on a weekly basis.
Are there any other ways to diagnose what is going wrong here?  Or any other changes that might be made?

            ## Accepted Answer
            I was unable to determine the cause of these crashes.  I resolved this by reinstalling the guest in a new virtual disk.  For the crashing VM, I had converted it from a VirtualBox image that an employee had created.  I suspect that was the cause of the problem.

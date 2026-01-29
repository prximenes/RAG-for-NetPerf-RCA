---
            {
  "source": "stackexchange",
  "license": "CC BY-SA 4.0 (Stack Exchange)",
  "site": "serverfault",
  "question_id": 805992,
  "link": "https://serverfault.com/questions/805992/is-vlan-tagging-on-guest-allowed-in-sr-iov-on-kvm",
  "score": 2,
  "views": 8704,
  "answer_id": 806783,
  "tags": [
    "kvm-virtualization",
    "vlan",
    "sr-iov"
  ],
  "query_label": "sriov-vlan-tagging-guest",
  "description": "Guest VLAN tagging constraints with SR-IOV; relevant to VF/PF policy and drops",
  "collected_at": "2025-12-13T15:57:37.437310+00:00"
}
            ---
            # Is vlan tagging on guest allowed in sr-iov on KVM?

            ## Question
            I am using KVM on Centos 7. I have created a VM with SR-IOV VFs to pass traffic. I notice that I am unable to pass traffic when I tag the interface inside the VM. I have read through the internet and the data sheet from Intel but none give me a clear picture of how it is done.
Server1
Eth0 - PF
SR-IOV Enabled
eth0-vf-1 (Attached to VM)
[Inside the VM]
Centos 7
eth0.100
Server2
Eth0 - PF
SR-IOV Enabled
eth0-vf-1 (Attached to VM)
[Inside the VM]
Centos 7
eth0.100
Switch
Extreme Networks
VLAN tagged 100
Port 1,2
Port 1 - Server 1 - Eth0 - PF
Port 2 - Server 2 - Eth0 - PF
Can anyone guide me through this? I would like to know if anyone has tried such a configuration or would this not be the best used case for SR-IOV?
I did find one issue here but did not understand much. Thank you community.

            ## Accepted Answer
            I checked, and it looks like with VFs, the tagging needs to be done on the host, via libvirt. The way this looks in the domxml is as follows
```
```
<interface type='hostdev' managed='yes'>
  <mac address=' fa:aa:aa:aa:aa:aa '/>
  <driver name='kvm'/>
  <source>
    <address type='pci' domain='0x0000' bus='0x02' slot='0x00' function='0x7'/>
  </source>
  <vlan>
    <tag id='190'/>
  </vlan>
  <alias name='hostdev0'/>
  <address type='pci' domain='0x0000' bus='0x00' slot='0x04' function='0x0'/>
</interface>
```
```
Link: https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Virtualization_Host_Configuration_and_Guest_Installation_Guide/sect-Virtualization_Host_Configuration_and_Guest_Installation_Guide-SR_IOV-How_SR_IOV_Libvirt_Works.html

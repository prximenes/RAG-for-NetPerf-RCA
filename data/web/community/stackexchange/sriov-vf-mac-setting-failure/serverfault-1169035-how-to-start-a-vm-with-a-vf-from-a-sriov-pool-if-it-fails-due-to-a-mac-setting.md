---
            {
  "source": "stackexchange",
  "license": "CC BY-SA 4.0 (Stack Exchange)",
  "site": "serverfault",
  "question_id": 1169035,
  "link": "https://serverfault.com/questions/1169035/how-to-start-a-vm-with-a-vf-from-a-sriov-pool-if-it-fails-due-to-a-mac-setting",
  "score": 0,
  "views": 297,
  "answer_id": 1169523,
  "tags": [
    "kvm-virtualization",
    "qemu",
    "infiniband",
    "sr-iov"
  ],
  "query_label": "sriov-vf-mac-setting-failure",
  "description": "VM start failures due to VF MAC settings; relevant to spoofchk/trust-like policy failures",
  "collected_at": "2025-12-13T15:57:39.350436+00:00"
}
            ---
            # How to start a VM with a VF from a SRIOV pool if it fails due to a MAC setting?

            ## Question
            I'm trying to run a KVM/QEMU VM under RHEL9 that uses a virtualized Infiniband card (VF) through SR-IOV from a pool of VFs.
I can specify a certain VF's PCI device with hostdev and that works just fine, however that requires hardcoding the PCI bus/slot/etc. into the VM XML sheet. That'd be a problem when migrating the VM to another server. So I'd rather define a network pool of VFs as described in this RH doc that would assign a free VF to a newly started VM automatically.
I did everything as described in the docs and the network pool of 8 VFs from a single IB card works like it should:
```
```
# virsh net-dumpxml IB-passthrough
<network>
  <name>IB-passthrough</name>
  <uuid>8dce28fa-97ea-43d4-a82b-5923fa1a2a4f</uuid>
  <forward mode='hostdev' managed='yes'>
    <address type='pci' domain='0x0000' bus='0xc1' slot='0x00' function='0x1'/>
    <address type='pci' domain='0x0000' bus='0xc1' slot='0x00' function='0x2'/>
    <address type='pci' domain='0x0000' bus='0xc1' slot='0x00' function='0x3'/>
    <address type='pci' domain='0x0000' bus='0xc1' slot='0x00' function='0x4'/>
    <address type='pci' domain='0x0000' bus='0xc1' slot='0x00' function='0x5'/>
    <address type='pci' domain='0x0000' bus='0xc1' slot='0x00' function='0x6'/>
    <address type='pci' domain='0x0000' bus='0xc1' slot='0x00' function='0x7'/>
    <address type='pci' domain='0x0000' bus='0xc1' slot='0x01' function='0x0'/>
  </forward>
</network>
```
```
I write the following entry into the VM's XML:
```
```
<interface type='network'>
  <source network='IB-passthrough'/>
</interface>
```
```
But after closing the XML editor, the entry gets automatically extended with
```
mac
```
 and
```
address
```
 entries:
```
```
<interface type='network'>
  <mac address='52:54:00:44:db:0d'/>
  <source network='IB-passthrough'/>
  <address type='pci' domain='0x0000' bus='0x07' slot='0x00' function='0x0'/>
</interface>
```
```
Then the VM cannot be started since the MAC cannot be set:
```
```
# virsh start rhel9.2-testvm
    error: Failed to start domain 'rhel9.2-testvm'
    error: Cannot set interface MAC to 52:54:00:05:72:5c for ifname ibp193s0 vf 0: Operation not supported
```
```
Is there a way to omit that automatic MAC? Or the Interface MAC change? Or is there another problem that I'm missing?

            ## Accepted Answer
            I met the same error when running cmd:
virsh attach-interface vm1 hostdev 0000:81:00.2 --managed --persistent
error: Failed to attach interface
error: Cannot set interface MAC to 52:54:00:6f:a1:89 for ifname ibp129s0f0 vf 1: Operation not supported
This interface network pool seems doesn't work for IB(InfiniBand) cards it only works for ethernet cards, because setting a MAC to an IB card will fail. Only cant set node, policy and port.
$ ls  /sys/class/net/ibp129s0f0/device/sriov/0/
node  policy  port
Finally, I managed to add the VF device via cmd:
virt-xml vm1 --add-device --update --hostdev 0000:81:00.2
You need to treat the IB(InfiniBand) card as a normal PCI device, not an ethernet interface.
Refer to:
https://docs.nvidia.com/networking/display/mlnxofedv24101140lts/single+root+io+virtualization+(sr-iov)https://enterprise-support.nvidia.com/s/article/HowTo-Configure-SR-IOV-for-ConnectX-4-ConnectX-5-ConnectX-6-with-KVM-Ethernethttps://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_and_managing_virtualization/managing-virtual-devices_configuring-and-managing-virtualization#assembly_managing-virtual-devices-using-the-cli_managing-virtual-deviceshttps://manpages.ubuntu.com/manpages/xenial/man1/virt-xml.1.html

---
{
  "source": "web",
  "label": "kernel-pci-sriov-howto",
  "url": "https://kernel.org/doc/html/latest/PCI/pci-iov-howto.html",
  "description": "SR-IOV enablement and VF/PF concepts (relevant to spoofchk/trust scenarios)",
  "license": null,
  "collected_at": "2025-12-15"
}
---

# PCI Express I/O Virtualization Howto (excerpt)

SR-IOV makes one physical PCIe device appear as multiple devices:

- **PF**: Physical Function
- **VF**: Virtual Function

Enable/disable VFs via sysfs:

```text
echo <nr_virtfn> > /sys/bus/pci/devices/<DOMAIN:BUS:DEVICE.FUNCTION>/sriov_numvfs
echo 0 > /sys/bus/pci/devices/<DOMAIN:BUS:DEVICE.FUNCTION>/sriov_numvfs
```

This artifact uses SR-IOV concepts as part of the scenarios and retrieval KB.


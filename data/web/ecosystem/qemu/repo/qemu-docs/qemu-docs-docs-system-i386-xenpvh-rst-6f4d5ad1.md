---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/system/i386/xenpvh.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.356512+00:00"
}
                    ---
                    # docs/system/i386/xenpvh.rst

                    Xen PVH machine (``xenpvh``)
=========================================

Xen supports a spectrum of types of guests that vary in how they depend
on HW virtualization features, emulation models and paravirtualization.
PVH is a mode that uses HW virtualization features (like HVM) but tries
to avoid emulation models and instead use passthrough or
paravirtualized devices.

QEMU can be used to provide PV virtio devices on an emulated PCIe controller.
That is the purpose of this minimal machine.

Supported devices
-----------------

The x86 Xen PVH QEMU machine provide the following devices:

- RAM
- GPEX host bridge
- virtio-pci devices

The idea is to only connect virtio-pci devices but in theory any compatible
PCI device model will work depending on Xen and guest support.

Running
-------

The Xen tools will typically construct a command-line and launch QEMU
for you when needed. But here's an example of what it can look like in
case you need to construct one manually:

.. code-block:: console

    qemu-system-i386 -xen-domid 3 -no-shutdown        \
      -chardev socket,id=libxl-cmd,path=/var/run/xen/qmp-libxl-3,server=on,wait=off \
      -mon chardev=libxl-cmd,mode=control             \
      -chardev socket,id=libxenstat-cmd,path=/var/run/xen/qmp-libxenstat-3,server=on,wait=off \
      -mon chardev=libxenstat-cmd,mode=control        \
      -nodefaults                                     \
      -no-user-config                                 \
      -xen-attach -name g0                            \
      -vnc none                                       \
      -display none                                   \
      -device virtio-net-pci,id=nic0,netdev=net0,mac=00:16:3e:5c:81:78 \
      -netdev type=tap,id=net0,ifname=vif3.0-emu,br=xenbr0,script=no,downscript=no \
      -smp 4,maxcpus=4                                \
      -nographic                                      \
      -machine xenpvh,ram-low-base=0,ram-low-size=2147483648,ram-high-base=4294967296,ram-high-size=2147483648,pci-ecam-base=824633720832,pci-ecam-size=268435456,pci-mmio-base=4026531840,pci-mmio-size=33554432,pci-mmio-high-base=824902156288,pci-mmio-high-size=68719476736 \
      -m 4096

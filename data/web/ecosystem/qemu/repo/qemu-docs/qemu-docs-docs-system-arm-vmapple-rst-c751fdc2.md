---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/system/arm/vmapple.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.349930+00:00"
}
                    ---
                    # docs/system/arm/vmapple.rst

                    .. SPDX-License-Identifier: GPL-2.0-or-later

VMApple machine emulation
========================================================================================

VMApple is the device model that the macOS built-in hypervisor called "Virtualization.framework"
exposes to Apple Silicon macOS guests. The "vmapple" machine model in QEMU implements the same
device model, but does not use any code from Virtualization.Framework.

Prerequisites
-------------

To run the vmapple machine model, you need to

 * Run on Apple Silicon
 * Run on macOS 12.0 or above
 * Have an already installed copy of a Virtualization.Framework macOS 12 virtual
   machine. Note that newer versions than 12.x are currently NOT supported on
   the guest side. I will assume that you installed it using the
   `macosvm <https://github.com/s-u/macosvm>`__ CLI.

First, we need to extract the UUID from the virtual machine that you installed. You can do this
by running the shell script in contrib/vmapple/uuid.sh on the macosvm.json file.

.. code-block:: bash
  :caption: uuid.sh script to extract the UUID from a macosvm.json file

  $ contrib/vmapple/uuid.sh "path/to/macosvm.json"

Now we also need to trim the aux partition. It contains metadata that we can just discard:

.. code-block:: bash
  :caption: Command to trim the aux file

  $ dd if="aux.img" of="aux.img.trimmed" bs=$(( 0x4000 )) skip=1

How to run
----------

Then, we can launch QEMU with the Virtualization.Framework pre-boot environment and the readily
installed target disk images. I recommend to port forward the VM's ssh and vnc ports to the host
to get better interactive access into the target system:

.. code-block:: bash
  :caption: Example execution command line

  $ UUID="$(contrib/vmapple/uuid.sh 'macosvm.json')"
  $ AVPBOOTER="/System/Library/Frameworks/Virtualization.framework/Resources/AVPBooter.vmapple2.bin"
  $ AUX="aux.img.trimmed"
  $ DISK="disk.img"
  $ qemu-system-aarch64 \
       -serial mon:stdio \
       -m 4G \
       -accel hvf \
       -M vmapple,uuid="$UUID" \
       -bios "$AVPBOOTER" \
       -drive file="$AUX",if=pflash,format=raw \
       -drive file="$DISK",if=pflash,format=raw \
       -drive file="$AUX",if=none,id=aux,format=raw \
       -drive file="$DISK",if=none,id=root,format=raw \
       -device vmapple-virtio-blk-pci,variant=aux,drive=aux \
       -device vmapple-virtio-blk-pci,variant=root,drive=root \
       -netdev user,id=net0,ipv6=off,hostfwd=tcp::2222-:22,hostfwd=tcp::5901-:5900 \
       -device virtio-net-pci,netdev=net0

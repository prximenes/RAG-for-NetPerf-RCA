---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/xen-save-devices-state.txt",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.214884+00:00"
}
                    ---
                    # docs/xen-save-devices-state.txt

                    = Save Devices =

QEMU has code to load/save the state of the guest that it is running.
These are two complementary operations.  Saving the state just does
that, saves the state for each device that the guest is running.

These operations are normally used with migration (see migration.txt),
however it is also possible to save the state of all devices to file,
without saving the RAM or the block devices of the VM.

The save operation is available as QMP command xen-save-devices-state.


The binary format used in the file is the following:


-------------------------------------------

32 bit big endian: QEMU_VM_FILE_MAGIC
32 bit big endian: QEMU_VM_FILE_VERSION

for_each_device
{
    8 bit:              QEMU_VM_SECTION_FULL
    32 bit big endian:  section_id
    8 bit:              idstr (ID string) length
    string:             idstr (ID string)
    32 bit big endian:  instance_id
    32 bit big endian:  version_id
    buffer:             device specific data
}

8 bit: QEMU_VM_EOF

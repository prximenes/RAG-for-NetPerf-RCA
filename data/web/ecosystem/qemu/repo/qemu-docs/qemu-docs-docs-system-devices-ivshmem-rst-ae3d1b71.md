---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/system/devices/ivshmem.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.335085+00:00"
}
                    ---
                    # docs/system/devices/ivshmem.rst

                    Inter-VM Shared Memory device
-----------------------------

On Linux hosts, a shared memory device is available. The basic syntax
is:

.. parsed-literal::

   |qemu_system_x86| -device ivshmem-plain,memdev=hostmem

where hostmem names a host memory backend. For a POSIX shared memory
backend, use something like

::

   -object memory-backend-file,size=1M,share,mem-path=/dev/shm/ivshmem,id=hostmem

If desired, interrupts can be sent between guest VMs accessing the same
shared memory region. Interrupt support requires using a shared memory
server and using a chardev socket to connect to it. The code for the
shared memory server is qemu.git/contrib/ivshmem-server. An example
syntax when using the shared memory server is:

.. parsed-literal::

   # First start the ivshmem server once and for all
   ivshmem-server -p pidfile -S path -m shm-name -l shm-size -n vectors

   # Then start your qemu instances with matching arguments
   |qemu_system_x86| -device ivshmem-doorbell,vectors=vectors,chardev=id
                    -chardev socket,path=path,id=id

When using the server, the guest will be assigned a VM ID (>=0) that
allows guests using the same server to communicate via interrupts.
Guests can read their VM ID from a device register (see
:doc:`../../specs/ivshmem-spec`).

Migration with ivshmem
~~~~~~~~~~~~~~~~~~~~~~

With device property ``master=on``, the guest will copy the shared
memory on migration to the destination host. With ``master=off``, the
guest will not be able to migrate with the device attached. In the
latter case, the device should be detached and then reattached after
migration using the PCI hotplug support.

At most one of the devices sharing the same memory can be master. The
master must complete migration before you plug back the other devices.

ivshmem and hugepages
~~~~~~~~~~~~~~~~~~~~~

Instead of specifying the <shm size> using POSIX shm, you may specify a
memory backend that has hugepage support:

.. parsed-literal::

   |qemu_system_x86| -object memory-backend-file,size=1G,mem-path=/dev/hugepages/my-shmem-file,share,id=mb1
                    -device ivshmem-plain,memdev=mb1

ivshmem-server also supports hugepages mount points with the ``-m``
memory path argument.

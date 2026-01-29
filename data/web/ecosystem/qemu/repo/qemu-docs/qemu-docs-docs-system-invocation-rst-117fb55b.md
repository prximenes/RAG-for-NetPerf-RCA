---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/system/invocation.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.277133+00:00"
}
                    ---
                    # docs/system/invocation.rst

                    .. _sec_005finvocation:

Invocation
----------

.. parsed-literal::

   |qemu_system| [options] [disk_image]

disk_image is a raw hard disk image for IDE hard disk 0. Some targets do
not need a disk image.

When dealing with options parameters as arbitrary strings containing
commas, such as in "file=my,file" and "string=a,b", it's necessary to
double the commas. For instance,"-fw_cfg name=z,string=a,,b" will be
parsed as "-fw_cfg name=z,string=a,b".

.. hxtool-doc:: qemu-options.hx

Device URL Syntax
~~~~~~~~~~~~~~~~~

.. include:: device-url-syntax.rst.inc

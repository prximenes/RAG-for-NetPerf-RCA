---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/system/arm/xlnx-zcu102.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.353749+00:00"
}
                    ---
                    # docs/system/arm/xlnx-zcu102.rst

                    Xilinx ZynqMP ZCU102 (``xlnx-zcu102``)
======================================

The ``xlnx-zcu102`` board models the Xilinx ZynqMP ZCU102 board.
This board has 4 Cortex-A53 CPUs and 2 Cortex-R5F CPUs.

Machine-specific options
""""""""""""""""""""""""

The following machine-specific options are supported:

secure
  Set ``on``/``off`` to enable/disable emulating a guest CPU which implements the
  Arm Security Extensions (TrustZone). The default is ``off``.

virtualization
  Set ``on``/``off`` to enable/disable emulating a guest CPU which implements the
  Arm Virtualization Extensions. The default is ``off``.

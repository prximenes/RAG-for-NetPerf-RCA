---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/system/confidential-guest-support.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.286083+00:00"
}
                    ---
                    # docs/system/confidential-guest-support.rst

                    Confidential Guest Support
==========================

Traditionally, hypervisors such as QEMU have complete access to a
guest's memory and other state, meaning that a compromised hypervisor
can compromise any of its guests.  A number of platforms have added
mechanisms in hardware and/or firmware which give guests at least some
protection from a compromised hypervisor.  This is obviously
especially desirable for public cloud environments.

These mechanisms have different names and different modes of
operation, but are often referred to as Secure Guests or Confidential
Guests.  We use the term "Confidential Guest Support" to distinguish
this from other aspects of guest security (such as security against
attacks from other guests, or from network sources).

Running a Confidential Guest
----------------------------

To run a confidential guest you need to add two command line parameters:

1. Use ``-object`` to create a "confidential guest support" object.  The
   type and parameters will vary with the specific mechanism to be
   used
2. Set the ``confidential-guest-support`` machine parameter to the ID of
   the object from (1).

Example (for AMD SEV)::

    qemu-system-x86_64 \
        <other parameters> \
        -machine ...,confidential-guest-support=sev0 \
        -object sev-guest,id=sev0,cbitpos=47,reduced-phys-bits=1

Supported mechanisms
--------------------

Currently supported confidential guest mechanisms are:

* AMD Secure Encrypted Virtualization (SEV) (see :doc:`i386/amd-memory-encryption`)
* Intel Trust Domain Extension (TDX) (see :doc:`i386/tdx`)
* POWER Protected Execution Facility (PEF) (see :ref:`power-papr-protected-execution-facility-pef`)
* s390x Protected Virtualization (PV) (see :doc:`s390x/protvirt`)

Other mechanisms may be supported in future.

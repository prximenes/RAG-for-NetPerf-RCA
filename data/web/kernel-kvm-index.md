---
                {
  "source": "web",
  "label": "kernel-kvm-index",
  "url": "https://www.kernel.org/doc/html/latest/virt/kvm/index.html",
  "description": "Kernel KVM documentation index (virtualization core)",
  "license": null,
  "collected_at": "2025-12-15T17:15:26.021348+00:00"
}
                ---
                # Linux Kernel documentation — KVM

                KVM — The Linux Kernel  documentation
The Linux Kernel
6.19.0-rc1
Quick search
document.getElementById('searchbox').style.display = "block"Contents
- Development process
- Submitting patches
- Code of conduct
- Maintainer handbook
- All development-process docs
- Core API
- Driver APIs
- Subsystems
- Core subsystems
- Human interfaces
- Networking interfaces
- Storage interfaces
- Other subsystems
- Accounting
- CPUFreq - CPU frequency and voltage scaling code in the Linux(TM) kernel
- EDAC Subsystem
- FPGA
- I2C/SMBus Subsystem
- Industrial I/O
- PCMCIA
- Serial Peripheral Interface (SPI)
- 1-Wire Subsystem
- Watchdog Support
- Virtualization Support
- Hardware Monitoring
- Compute Accelerators
- Security Documentation
- Crypto API
- BPF Documentation
- USB support
- PCI Bus Subsystem
- Assorted Miscellaneous Devices Documentation
- PECI Subsystem
- WMI Subsystem
- TEE Subsystem
- Locking
- Licensing rules
- Writing documentation
- Development tools
- Testing guide
- Hacking guide
- Tracing
- Fault injection
- Livepatching
- Rust
- Administration
- Build system
- Reporting issues
- Userspace tools
- Userspace API
- Firmware
- Firmware and Devicetree
- CPU architectures
- Unsorted documentation
- Translations
 <!--
  var sbar = document.getElementsByClassName("sphinxsidebar")[0];
  let currents = document.getElementsByClassName("current")
  if (currents.length) {
    sbar.scrollTop = currents[currents.length - 1].offsetTop;
  }
  --> This Page
- Show Source
KVM¶
- The Definitive KVM (Kernel-based Virtual Machine) API Documentation
- 1. General description
- 2. Restrictions
- 3. Extensions
- 4. API description
- 5. The kvm_run structure
- 6. Capabilities that can be enabled on vCPUs
- 7. Capabilities that can be enabled on VMs
- 8. Other capabilities.
- 9. Known KVM API problems
- Devices
- ARM Virtual Interrupt Translation Service (ITS)
- ARM Virtual Generic Interrupt Controller v2 (VGIC)
- ARM Virtual Generic Interrupt Controller v3 and later (VGICv3)
- MPIC interrupt controller
- FLIC (floating interrupt controller)
- Generic vcpu interface
- VFIO virtual device
- Generic vm interface
- XICS interrupt controller
- POWER9 eXternal Interrupt Virtualization Engine (XIVE Gen1)
- ARM
- ARM firmware pseudo-registers interface
- Internal ABI between the kernel and HYP
- KVM/arm64-specific hypercalls exposed to guests
- Paravirtualized time support for arm64
- PTP_KVM support for arm/arm64
- vCPU feature selection on arm64
- KVM for s390 systems
- The s390 DIAGNOSE call on KVM
- s390 (IBM Z) Ultravisor and Protected VMs
- s390 (IBM Z) Boot/IPL of Protected VMs
- s390 (IBM Z) Protected Virtualization dumps
- The PPC KVM paravirtual interface
- Querying for existence
- KVM hypercalls
- The magic page
- Magic page features
- Magic page flags
- MSR bits
- Patched instructions
- Hypercall ABIs in KVM on PowerPC
- KVM for x86 systems
- Secure Encrypted Virtualization (SEV)
- KVM CPUID bits
- Known limitations of CPU virtualization
- Linux KVM Hypercall
- Intel Trust Domain Extensions (TDX)
- The x86 kvm shadow mmu
- KVM-specific MSRs
- Nested VMX
- Running nested guests with KVM
- Timekeeping Virtualization for X86-Based Architectures
- KVM for LoongArch systems
- The LoongArch paravirtual interface
- KVM Lock Overview
- 1. Acquisition Orders
- 2. Exception
- 3. Reference
- KVM VCPU Requests
- Overview
- VCPU Request Internals
- VCPU Requests with Associated State
- Ensuring Requests Are Seen
- Additional Considerations
- References
- The KVM halt polling system
- Halt Polling Interval
- Module Parameters
- KVM_CAP_HALT_POLL
- Further Notes
- Review checklist for kvm patches
- Testing of KVM code
      ©The kernel development community.
      |
      Powered by Sphinx 5.3.0
      & Alabaster 0.7.16
      |
      Page source

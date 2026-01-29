---
                {
  "source": "web",
  "label": "kernel-bpf-index",
  "url": "https://www.kernel.org/doc/html/latest/bpf/index.html",
  "description": "Kernel BPF/XDP docs relevant to XDP packet loss and performance scenarios",
  "license": null,
  "collected_at": "2025-12-15T17:15:17.429553+00:00"
}
                ---
                # Linux Kernel BPF Documentation (Index)

                BPF Documentation — The Linux Kernel  documentation
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
BPF Documentation¶
This directory contains documentation for the BPF (Berkeley Packet
Filter) facility, with a focus on the extended BPF version (eBPF).
This kernel side documentation is still work in progress.
The Cilium project also maintains a BPF and XDP Reference Guide
that goes into great technical depth about the BPF Architecture.
- eBPF verifier
- libbpf
- BPF Standardization
- BPF Type Format (BTF)
- Frequently asked questions (FAQ)
- Syscall API
- Helper functions
- BPF Kernel Functions (kfuncs)
- BPF cpumask kfuncs
- BPF filesystem kfuncs
- Program Types
- BPF maps
- Running BPF programs from userspace
- Classic BPF vs eBPF
- BPF Iterators
- BPF licensing
- Testing and debugging BPF
- 1 Clang implementation notes
- 1 Linux implementation notes
- Other
- Redirect
      ©The kernel development community.
      |
      Powered by Sphinx 5.3.0
      & Alabaster 0.7.16
      |
      Page source

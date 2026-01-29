---
                {
  "source": "web",
  "label": "dpdk-linux-gsg",
  "url": "https://doc.dpdk.org/guides/linux_gsg/index.html",
  "description": "Hugepages, drivers, build/run basics; supports DPDK deployment troubleshooting scenarios",
  "license": "DPDK docs (see site for license)",
  "collected_at": "2025-12-15T17:15:34.745447+00:00"
}
                ---
                # DPDK Getting Started Guide for Linux

                Getting Started Guide for Linux — Data Plane Development Kit 25.11.0 documentation
            Data Plane Development Kit
                25.11.0
- Getting Started Guide for Linux
- 1. Introduction
- 2. System Requirements
- 3. Compiling the DPDK Target from Source
- 4. Cross compiling DPDK for aarch64 and aarch32
- 5. Cross compiling DPDK for LoongArch
- 6. Cross compiling DPDK for RISC-V
- 7. Linux Drivers
- 8. Running Sample Applications
- 9. EAL parameters
- 10. Enabling Additional Functionality
- 11. How to get best performance with NICs on Intel platforms
- 12. How to get best performance on AMD platform
- Getting Started Guide for FreeBSD
- Getting Started Guide for Windows
- Sample Applications User Guides
- Programmerâs Guide
- HowTo Guides
- DPDK Tools User Guides
- Testpmd Application User Guide
- Network Interface Controller Drivers
- Baseband Device Drivers
- Crypto Device Drivers
- Compression Device Drivers
- vDPA Device Drivers
- REGEX Device Drivers
- Machine Learning Device Driver
- DMA Device Drivers
- General-Purpose Graphics Processing Unit Drivers
- Event Device Drivers
- Rawdev Drivers
- Mempool Device Driver
- Platform Specific Guides
- Contributorâs Guidelines
- Release Notes
- FAQ
Data Plane Development Kit
-
- Getting Started Guide for Linux
-  View page source
Getting Started Guide for Linux
- 1. Introduction
- 1.1. Documentation Roadmap
- 2. System Requirements
- 2.1. BIOS Setting Prerequisite on x86
- 2.2. Compilation of the DPDK
- 2.3. Running DPDK Applications
- 3. Compiling the DPDK Target from Source
- 3.1. Uncompress DPDK and Browse Sources
- 3.2. Compiling and Installing DPDK System-wide
- 4. Cross compiling DPDK for aarch64 and aarch32
- 4.1. Prerequisites
- 4.2. GNU toolchain
- 4.3. LLVM/Clang toolchain
- 4.4. Building for an aarch64 SoC on an aarch64 build machine
- 4.5. Supported SoC configuration
- 5. Cross compiling DPDK for LoongArch
- 5.1. Prerequisites
- 5.2. GNU toolchain
- 5.3. Supported cross-compilation targets
- 6. Cross compiling DPDK for RISC-V
- 6.1. Prerequisites
- 6.2. GNU toolchain
- 6.3. Supported cross-compilation targets
- 7. Linux Drivers
- 7.1. Binding and Unbinding Network Ports to/from the Kernel Modules
- 7.2. VFIO
- 7.3. VFIO Platform
- 7.4. Bifurcated Driver
- 7.5. UIO
- 8. Running Sample Applications
- 8.1. Compiling a Sample Application
- 8.2. Running a Sample Application
- 8.3. Additional Sample Applications
- 9. EAL parameters
- 9.1. Common EAL parameters
- 9.2. Linux-specific EAL parameters
- 10. Enabling Additional Functionality
- 10.1. Running DPDK Applications Without Root Privileges
- 10.2. Power Management and Power Saving Functionality
- 10.3. Using Linux Core Isolation to Reduce Context Switches
- 10.4. High Precision Event Timer (HPET) Functionality
- 11. How to get best performance with NICs on Intel platforms
- 11.1. Hardware and Memory Requirements
- 11.2. Configurations before running DPDK
- 12. How to get best performance on AMD platform
- 12.1. Tuning Guides for AMD EPYC SoC
- 12.2. General Requirements
- 12.3. BIOS
- 12.4. Linux GRUB
- 12.5. NIC and Accelerator
- 12.6. Compiler
- 12.7. Max LCores
- 12.8. Power
- 12.9. NIC
 PreviousNext
  Built with Sphinx using a
    theme
    provided by Read the Docs.
      jQuery(function () {
          SphinxRtdTheme.Navigation.enable(true);
      });

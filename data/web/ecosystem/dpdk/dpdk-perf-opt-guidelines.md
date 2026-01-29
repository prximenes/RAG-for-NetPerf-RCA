---
                {
  "source": "web",
  "label": "dpdk-perf-opt-guidelines",
  "url": "https://doc.dpdk.org/guides/prog_guide/perf_opt_guidelines.html",
  "description": "High-signal performance guidance (cache/NUMA/mtune patterns); supports DPDK throughput/drop scenarios",
  "license": "DPDK docs (see site for license)",
  "collected_at": "2025-12-15T17:15:35.075270+00:00"
}
                ---
                # DPDK Performance Optimization Guidelines

                1. Performance Optimization Guidelines — Data Plane Development Kit 25.11.0 documentation
            Data Plane Development Kit
                25.11.0
- Getting Started Guide for Linux
- Getting Started Guide for FreeBSD
- Getting Started Guide for Windows
- Sample Applications User Guides
- Programmerâs Guide
- Foundation Principles
- Memory Management
- CPU Management
- CPU Packet Processing
- Device Libraries
- Protocol Processing Libraries
- High-Level Libraries
- Utility Libraries
- Howto Guides
- Tips & Tricks
- 1. Performance Optimization Guidelines
- 1.1. Introduction
- 2. Writing Efficient Code
- 3. Link Time Optimization
- 4. Profile Your Application
- 5. Running AddressSanitizer
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
- Programmerâs Guide
- 1. Performance Optimization Guidelines
-  View page source
1. Performance Optimization Guidelines
1.1. Introduction
The following sections describe optimizations used in DPDK and optimizations that should be considered for new applications.
They also highlight the performance-impacting coding techniques that should,
and should not be, used when developing an application using the DPDK.
And finally, they give an introduction to application profiling using a Performance Analyzer from Intel to optimize the software.
 PreviousNext
  Built with Sphinx using a
    theme
    provided by Read the Docs.
      jQuery(function () {
          SphinxRtdTheme.Navigation.enable(true);
      });

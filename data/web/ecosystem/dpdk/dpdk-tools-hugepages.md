---
                {
  "source": "web",
  "label": "dpdk-tools-hugepages",
  "url": "https://doc.dpdk.org/guides/tools/hugepages.html",
  "description": "Hugepages management tool reference; supports DPDK allocation/setup troubleshooting",
  "license": "DPDK docs (see site for license)",
  "collected_at": "2025-12-15T17:15:35.407869+00:00"
}
                ---
                # dpdk-hugepages tool

                1. dpdk-hugepages Application — Data Plane Development Kit 25.11.0 documentation
            Data Plane Development Kit
                25.11.0
- Getting Started Guide for Linux
- Getting Started Guide for FreeBSD
- Getting Started Guide for Windows
- Sample Applications User Guides
- Programmerâs Guide
- HowTo Guides
- DPDK Tools User Guides
- 1. dpdk-hugepages Application
- 1.1. Running the Application
- 1.2. Options
- 1.3. Examples
- 2. dpdk-devbind Application
- 3. dpdk-proc-info Application
- 4. dpdk-pmdinfo Application
- 5. dpdk-dumpcap Application
- 6. dpdk-pdump Application
- 7. dpdk-test-dma-perf Application
- 8. Flow Performance Tool
- 9. Security Performance Tool
- 10. dpdk-test-bbdev Application
- 11. dpdk-test-crypto-perf Application
- 12. dpdk-test-compress-perf Tool
- 13. dpdk-test-eventdev Application
- 14. dpdk-test-regex Tool
- 15. dpdk-test-mldev Application
- 16. dpdk-graph Application
- 17. DPDK Test Suite
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
- DPDK Tools User Guides
- 1. dpdk-hugepages Application
-  View page source
1. dpdk-hugepages Application
The
```
dpdk-hugepages
```
 tool is a Data Plane Development Kit (DPDK) utility
that helps in reserving hugepages.
As well as checking for current settings.
1.1. Running the Application
The tool has a number of command line options:
```
dpdk-hugepages [options]
```
1.2. Options
-
```
-h,--help
```
Display usage information and quit
-
```
-s,--show
```
Print the current huge page configuration
-
```
-cdriver,--clear
```
Clear existing huge page reservation
-
```
-m,--mount
```
Mount the huge page filesystem
-
```
-u,--unmount
```
Unmount the huge page filesystem
-
```
-nNODE,--node=NODE
```
Set NUMA node to reserve pages on
-
```
-pSIZE,--pagesize=SIZE
```
Select hugepage size to use.If not specified the default system huge page size is used.
-
```
-rSIZE,--reserve=SIZE
```
Reserve huge pages.Size is in bytes with K, M or G suffix.
-
```
--setupSIZE
```
Short cut to clear, unmount, reserve and mount.
Warning
While any user can run the
```
dpdk-hugepages.py
```
 script to view the
status of huge pages, modifying the setup requires root privileges.
1.3. Examples
To display current huge page settings:
```
dpdk-hugepages.py -s
```
To a complete setup of with 2 Gigabyte of 1G huge pages:
```
dpdk-hugepages.py -p 1G --setup 2G
```
 PreviousNext
  Built with Sphinx using a
    theme
    provided by Read the Docs.
      jQuery(function () {
          SphinxRtdTheme.Navigation.enable(true);
      });

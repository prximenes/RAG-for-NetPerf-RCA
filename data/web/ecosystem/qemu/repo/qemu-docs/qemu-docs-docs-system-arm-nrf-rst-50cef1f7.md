---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/system/arm/nrf.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.351002+00:00"
}
                    ---
                    # docs/system/arm/nrf.rst

                    Nordic nRF boards (``microbit``)
================================

The `Nordic nRF`_ chips are a family of ARM-based System-on-Chip that
are designed to be used for low-power and short-range wireless solutions.

.. _Nordic nRF: https://www.nordicsemi.com/Products

The nRF51 series is the first series for short range wireless applications.
It is superseded by the nRF52 series.
The following machines are based on this chip :

- ``microbit``       BBC micro:bit board with nRF51822 SoC

There are other series such as nRF52, nRF53 and nRF91 which are currently not
supported by QEMU.

Supported devices
-----------------

 * ARM Cortex-M0 (ARMv6-M)
 * Serial ports (UART)
 * Clock controller
 * Timers
 * Random Number Generator (RNG)
 * GPIO controller
 * NVMC
 * SWI

Missing devices
---------------

 * Watchdog
 * Real-Time Clock (RTC) controller
 * TWI (i2c)
 * SPI controller
 * Analog to Digital Converter (ADC)
 * Quadrature decoder
 * Radio

Boot options
------------

The Micro:bit machine can be started using the ``-device`` option to load a
firmware in `ihex format`_. Example:

.. _ihex format: https://en.wikipedia.org/wiki/Intel_HEX

.. code-block:: bash

  $ qemu-system-arm -M microbit -device loader,file=test.hex

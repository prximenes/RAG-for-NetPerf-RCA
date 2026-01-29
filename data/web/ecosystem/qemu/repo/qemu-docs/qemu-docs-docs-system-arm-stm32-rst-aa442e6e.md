---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/system/arm/stm32.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.348603+00:00"
}
                    ---
                    # docs/system/arm/stm32.rst

                    STMicroelectronics STM32 boards (``netduino2``, ``netduinoplus2``, ``olimex-stm32-h405``, ``stm32vldiscovery``)
===============================================================================================================

The `STM32`_ chips are a family of 32-bit ARM-based microcontroller by
STMicroelectronics.

.. _STM32: https://www.st.com/en/microcontrollers-microprocessors/stm32-32-bit-arm-cortex-mcus.html

The STM32F1 series is based on ARM Cortex-M3 core. The following machines are
based on this chip :

- ``stm32vldiscovery``  STM32VLDISCOVERY board with STM32F100RBT6 microcontroller

The STM32F2 series is based on ARM Cortex-M3 core. The following machines are
based on this chip :

- ``netduino2``         Netduino 2 board with STM32F205RFT6 microcontroller

The STM32F4 series is based on ARM Cortex-M4F core, as well as the STM32L4
ultra-low-power series. The STM32F4 series is pin-to-pin compatible with STM32F2 series.
The following machines are based on this ARM Cortex-M4F chip :

- ``netduinoplus2``     Netduino Plus 2 board with STM32F405RGT6 microcontroller
- ``olimex-stm32-h405`` Olimex STM32 H405 board with STM32F405RGT6 microcontroller
- ``b-l475e-iot01a``     :doc:`B-L475E-IOT01A IoT Node </system/arm/b-l475e-iot01a>` board with STM32L475VG microcontroller

There are many other STM32 series that are currently not supported by QEMU.

Supported devices
-----------------

 * ARM Cortex-M3, Cortex M4F
 * Analog to Digital Converter (ADC)
 * EXTI interrupt
 * Serial ports (USART)
 * SPI controller
 * System configuration (SYSCFG)
 * Timer controller (TIMER)
 * Reset and Clock Controller (RCC) (STM32F4 only, reset and enable only)

Missing devices
---------------

 * Camera interface (DCMI)
 * Controller Area Network (CAN)
 * Cycle Redundancy Check (CRC) calculation unit
 * Digital to Analog Converter (DAC)
 * DMA controller
 * Ethernet controller
 * Flash Interface Unit
 * GPIO controller
 * I2C controller
 * Inter-Integrated Sound (I2S) controller
 * Power supply configuration (PWR)
 * Random Number Generator (RNG)
 * Real-Time Clock (RTC) controller
 * Reset and Clock Controller (RCC) (other features than reset and enable)
 * Secure Digital Input/Output (SDIO) interface
 * USB OTG
 * Watchdog controller (IWDG, WWDG)

Boot options
------------

The STM32 machines can be started using the ``-kernel`` option to load a
firmware. Example:

.. code-block:: bash

  $ qemu-system-arm -M stm32vldiscovery -kernel firmware.bin

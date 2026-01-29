---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/system/target-avr.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.288066+00:00"
}
                    ---
                    # docs/system/target-avr.rst

                    .. _AVR-System-emulator:

AVR System emulator
-------------------

Use the executable ``qemu-system-avr`` to emulate a AVR 8 bit based machine.
These can have one of the following cores: avr1, avr2, avr25, avr3, avr31,
avr35, avr4, avr5, avr51, avr6, avrtiny, xmega2, xmega3, xmega4, xmega5,
xmega6 and xmega7.

As for now it supports few Arduino boards for educational and testing purposes.
These boards use a ATmega controller, which model is limited to USART & 16-bit
timer devices, enough to run FreeRTOS based applications (like
https://github.com/seharris/qemu-avr-tests/blob/master/free-rtos/Demo/AVR_ATMega2560_GCC/demo.elf
).

Following are examples of possible usages, assuming demo.elf is compiled for
AVR cpu

- Continuous non interrupted execution::

   qemu-system-avr -machine mega2560 -bios demo.elf

- Continuous non interrupted execution with serial output into telnet window::

   qemu-system-avr -M mega2560 -bios demo.elf -nographic \
                   -serial tcp::5678,server=on,wait=off

  and then in another shell::

   telnet localhost 5678

- Debugging with GDB debugger::

   qemu-system-avr -machine mega2560 -bios demo.elf -s -S

  and then in another shell::

   avr-gdb demo.elf

  and then within GDB shell::

   target remote :1234

- Print out executed instructions (that have not been translated by the JIT
  compiler yet)::

   qemu-system-avr -machine mega2560 -bios demo.elf -d in_asm

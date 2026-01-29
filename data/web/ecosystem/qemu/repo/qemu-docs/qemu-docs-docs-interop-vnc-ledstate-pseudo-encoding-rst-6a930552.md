---
                    {
  "source": "docsrepo",
  "label": "qemu-docs",
  "repo_url": "https://github.com/qemu/qemu.git",
  "ref": "master",
  "commit": "9c23f2a7b0b45277693a14074b1aaa827eecdb92",
  "path_in_repo": "docs/interop/vnc-ledstate-pseudo-encoding.rst",
  "description": "QEMU documentation from upstream repository (docs/).",
  "license": "QEMU documentation (see QEMU repository for license)",
  "collected_at": "2025-12-15T17:38:11.244197+00:00"
}
                    ---
                    # docs/interop/vnc-ledstate-pseudo-encoding.rst

                    VNC LED state Pseudo-encoding
=============================

Introduction
------------

This document describes the Pseudo-encoding of LED state for RFB which
is the protocol used in VNC as reference link below:

http://tigervnc.svn.sourceforge.net/viewvc/tigervnc/rfbproto/rfbproto.rst?content-type=text/plain

When accessing a guest by console through VNC, there might be mismatch
between the lock keys notification LED on the computer running the VNC
client session and the current status of the lock keys on the guest
machine.

To solve this problem it attempts to add LED state Pseudo-encoding
extension to VNC protocol to deal with setting LED state.

Pseudo-encoding
---------------

This Pseudo-encoding requested by client declares to server that it supports
LED state extensions to the protocol.

The Pseudo-encoding number for LED state defined as:

======= ===============================================================
Number  Name
======= ===============================================================
-261    'LED state Pseudo-encoding'
======= ===============================================================

LED state Pseudo-encoding
--------------------------

The LED state Pseudo-encoding describes the encoding of LED state which
consists of 3 bits, from left to right each bit represents the Caps, Num,
and Scroll lock key respectively. '1' indicates that the LED should be
on and '0' should be off.

Some example encodings for it as following:

======= ===============================================================
Code    Description
======= ===============================================================
100     CapsLock is on, NumLock and ScrollLock are off
010     NumLock is on, CapsLock and ScrollLock are off
111     CapsLock, NumLock and ScrollLock are on
======= ===============================================================

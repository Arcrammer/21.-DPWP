#!/usr/bin/env python
# --------------------------
#   library.py
#   Reusable Library
#   Friday, 14 August, 2015
#   Alexander Rhett Crammer
#   Full Sail University
# --------------------------
#
class Device(object):
    def __init__(self):
        self.company = None # Device owner and seller (Samsung, Motorola, Apple, Nexus)
        self.model = None # id est iPhone, Galaxy, Chromebook, Modbook
        self.portable = None # Boolean value to represent portability (Desktops aren't portable but iPod's are)
        self.condition = None # Condition of the device (Old, New, Okay, Pitiful, Shattered like an iPhone)
        self.kind = None # Type of device (Tablet, Smartphone, Laptop, Desktop)
        self.operating_system = None # Operating system of the device (Fire OS, Android, iOS, Windows, Linux, OS X)

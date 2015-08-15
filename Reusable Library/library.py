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
        self.__company = None # Device owner and seller (Samsung, Motorola, Apple, Nexus)
        self.__model = None # id est iPhone, Galaxy, Chromebook, Modbook
        self.__portable = None # Boolean value to represent portability (Desktops aren't portable but iPod's are)
        self.__condition = None # Condition of the device (Old, New, Okay, Pitiful, Shattered like an iPhone)
        self.__kind = None # Type of device (Tablet, Smartphone, Laptop, Desktop)
        self.__operating_system = None # Operating system of the device (Fire OS, Android, iOS, Windows, Linux, OS X)

        # Getters
        @property
        def company(self):
            return self.__company

        @property
        def model(self):
            return self.__model

        @property
        def portable(self):
            return self.__portable

        @property
        def condition(self):
            return self.__condition

        @property
        def kind(self):
            return self.__kind

        @property
        def operating_system(self):
            return self.__operating_system

        # Setters
        @company.setter
        def company(self, desired_value):
            self.__company = desired_value

        @model.setter
        def model(self, desired_value):
            self.__model = desired_value

        @portable.setter
        def portable(self, desired_value):
            self.__portable = desired_value

        @condition.setter
        def condition(self, desired_value):
            self.__condition = desired_value

        @kind.setter
        def kind(self, desired_value):
            self.__kind = desired_value

        @operating_system.setter
        def operating_system(self, desired_value):
            self.__operating_system = desired_value


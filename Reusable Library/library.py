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
        self.__age = None # Integer representing the amount of years the device has accumulated age

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

        @property
        def age(self):
            return self.__age

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

        @age.setter
        def age(self, desired_value):
            self.__age = desired_value

# End of 'Device' Definition

class DeviceData(object):
    def __init__(self, devices):
        self.__devices = devices

    def add_device(self, device):
        self.__devices.append(device)

    def average(self):
        ''' Find the average age among the 'Device' objects '''
        ages = []
        total = float()
        for device in self.__devices:
            ages.append(device.age) # Add the age of the device to the 'age' array
            total += device.age # Add the age of the device to the 'total' float
        return total / len(ages) # Find the average based on the 'age' and 'total' values and return it

    def device_rows(self):
        ''' Render an HTML list containing information for each device '''
        list_source = "" # Empty string; 'tr' elements will be appended later within this method
        for device in self.__devices:
            # Each 'Device' object
            list_source += "<tr>" # Create a 'tr' element
            list_source += "<td>%s</td>" % ( device.company )
            list_source += "<td>%s</td>" % ( device.model )
            if device.portable:
                list_source += "<td>Yes</td>"
            else:
                list_source += "<td>No</td>"
            list_source += "<td>%s</td>" % ( device.condition )
            list_source += "<td>%s</td>" % ( device.kind )
            list_source += "<td>%s</td>" % ( device.operating_system )
            if device.age >= 1.1: # Just some pluralisation and word appropriation
                list_source += "<td>%s Years</td>" % ( device.age )
            elif device.age == 1:
                list_source += "<td>%s Year</td>" % ( device.age )
            else:
                list_source += "<td>%s Months</td>" % ( str(device.age).split(".")[-1] ) # Remove the leading 0
            list_source += "</tr>" # Close the 'tr' element for this device
        return list_source # Return the rows for all of the devices

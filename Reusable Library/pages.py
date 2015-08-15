#!/usr/bin/env python
# --------------------------
#   pages.py
#   Reusable Library
#   Friday, 14 August, 2015
#   Alexander Rhett Crammer
#   Full Sail University
# --------------------------
#
from library import DeviceData

class Welcome(object):
    def __init__(self):
        self.title = "Device Dashboard // Welcome"
        self.main_stylesheet_path = "Main.css"

    def render(self):
        ''' Return the response data '''
        return open("index.html","r").read().format(**locals()) # Interpolate template values and return the result as a string

class DeviceList(object):
    def __init__(self, devices):
        self.title = "Device Dashboard // Devices"
        self.main_stylesheet_path = "Main.css"
        self.devices = devices
        self.device_rows = DeviceData(devices).device_rows() # Ask the utility class for an HTML list of data for each device

    def render(self):
        ''' Return the response data '''
        return open("device_list.html","r").read().format(**locals()) # Interpolate template values and return the result as a string

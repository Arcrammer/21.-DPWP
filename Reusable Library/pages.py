#!/usr/bin/env python
# --------------------------
#   pages.py
#   Reusable Library
#   Friday, 14 August, 2015
#   Alexander Rhett Crammer
#   Full Sail University
# --------------------------
#
class Welcome(object):
    def __init__(self):
        self.title = "Some Page"
        self.main_stylesheet_path = "Main.css"

    def render(self):
        return open("index.html","r").read().format(**locals())

class DeviceList(object):
    def __init__(self, devices):
        self.title = "Some Page"
        self.main_stylesheet_path = "Main.css"
        print("Devices --------------------------")
        print(devices)

    def render(self):
        return open("device_list.html","r").read().format(**locals())

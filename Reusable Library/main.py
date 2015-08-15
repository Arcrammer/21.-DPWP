#!/usr/bin/env python
# --------------------------
#
#   main.py
#   Reusable Library
#   Friday, 14 August, 2015
#   Alexander Rhett Crammer
#   Full Sail University
#
# --------------------------
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# --------------------------
#
import webapp2
from pages import * # Import all classes from 'pages.py'
from library import * # Import all class from 'library.py'

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # Create an array to hold each Device() object
        devices = []

        # Create some Device() objects beginning with an iPhone
        iPhone = Device()
        iPhone.company = "Apple"
        iPhone.model = "iPhone 6 Plus"
        iPhone.portable = True
        iPhone.condition = "New"
        iPhone.kind = "Smartphone"
        iPhone.operating_system = "iOS 9 Beta 5"
        iPhone.age = 0.6
        devices.append(iPhone)

        # Let's make an iPad, too
        iPad = Device()
        iPad.company = "Apple"
        iPad.model = "iPad"
        iPad.portable = True
        iPad.condition = "New"
        iPad.kind = "Tablet"
        iPad.operating_system = "iOS 8"
        iPad.age = 1
        devices.append(iPad)

        # For good measure we'll make a desktop machine
        iMac = Device()
        iMac.company = "Apple"
        iMac.model = "iMac with 5K Retina Display"
        iMac.portable = False
        iMac.condition = "New"
        iMac.kind = "Desktop"
        iMac.operating_system = "10.11 El Capitan Beta 4"
        iMac.age = 1.4
        devices.append(iMac)

        # Create an instance of the devices page
        devices_page = DeviceList(devices)

        # Write the response to the browser
        self.response.write(devices_page.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

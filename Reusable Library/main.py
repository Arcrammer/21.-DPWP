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

        if self.request.GET:
            # The user has provided device data through the form

            # Create a Device() object with the form data provided
            user_device = Device()
            user_device.company = self.request.GET["company"]
            user_device.model = self.request.GET["model"]
            user_device.portable = self.request.GET["portable"]
            user_device.condition = self.request.GET["condition"]
            user_device.kind = self.request.GET["kind"]
            user_device.operating_system = self.request.GET["operating_system"]
            user_device.age = self.request.GET["age"]
            devices.append(user_device)

            # Create an instance of the devices page
            devices_page = DeviceList(devices)

            # Write the response to the browser
            self.response.write(devices_page.render())
        else:
            # The user has not provided any device data of their own, so we'll allow them to do so with a form

            # Write the response to the browser
            self.response.write(Welcome().render()) # Create an instance of the welcome page then send it to the browser

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

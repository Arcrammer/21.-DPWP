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
from pages import Welcome
from library import Device

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(Welcome().render())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

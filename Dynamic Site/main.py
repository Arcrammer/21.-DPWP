#!/usr/bin/env python
# --------------------------
#   main.py
#   Dynamic Site
#   Friday, 21 August, 2015
#   Alexander Rhett Crammer
#   Full Sail University
# --------------------------
# CONTROLLERS
#
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
#
import webapp2
from data import * # Import all classes from 'data.py'
from pages import * # Import all classes from 'pages.py'

class MainHandler(webapp2.RequestHandler):
    def get(self):
        if not self.request.GET:
            # The user has not requested to view information about a well known work of art, so we'll show them the default 'Credit' page
            response_page = Page() # Create a 'Page' instance
            response_page.title = "Credit"
        else:
            # The user has submitted GET data so we'll show them information of a well known artistic work
            response_page = FamousWorkPage() # Create a 'FamousWorkPage' instance
            work_of_art = Work() # We'll pass one of these to the 'FamousWorkPage' object
            work_of_art.art_name = self.request.get("work")
        self.response.write(response_page.render_view()) # Return the view to the client

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

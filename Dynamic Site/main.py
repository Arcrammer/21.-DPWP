#!/usr/bin/env python
# --------------------------
#   main.py
#   Dynamic Site
#   Friday, 21 August, 2015
#   Alexander Rhett Crammer
#   Full Sail University
# --------------------------
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
        welcome_page = WorkPage() # Create a 'WorkPage' instance
        work_of_art = Art()
        # IMPORTANT: Content from 'data.py' should be delegated to 'pages.py' here; Only this object should access MainHandler.request
        if self.request.get("work") == "Mona-Lisa":
            welcome_page.title = "Mona Lisa"
            welcome_page.view_name = "MonaLisa"
            work_of_art.artist = "Leonardo da Vinci"
            work_of_art.description = "Portrait of Lisa Gherardini, wife of Francesco del Giocondo, referred to as Monna Lisa, The Gioconda or The Joconde. Painted in Florence, Italy in the early 1500's."
            work_of_art.materials_used = "Oil Paint, Poplar Wood."
            work_of_art.image_name = "MonaLisa.jpg"
            welcome_page.art = work_of_art
        else:
            # No work has been asked for, so we'll show the credit of each asset
            welcome_page.title = "Credit"
            welcome_page.view_name = "Credit"
        self.response.write(welcome_page.render_view()) # Return the view to the client

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

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
        # IMPORTANT: Content from 'data.py' should be delegated to 'pages.py' here; Only this object should access MainHandler.request
        if self.request.GET:
            # The user has submitted GET data so we'll show them information of a well known artistic work
            response_page = FamousWorkPage() # Create a 'FamousWorkPage' instance
            work_of_art = Art() # We'll pass one of these to the 'WorkPage' object
        else:
            # The user has not requested to view information about a well known work of art, so we'll show them the default 'Credit' page
            response_page = Page() # Create a 'WorkPage' instance
            response_page.title = "Credit"
        if self.request.get("work") == "Mona-Lisa":
            response_page.title = "Mona Lisa"
            work_of_art.artist = "Leonardo da Vinci"
            work_of_art.time = "Early 1500's"
            work_of_art.description = "Portrait of Lisa Gherardini, wife of Francesco del Giocondo, referred to as Monna Lisa, The Gioconda or The Joconde. Painted in Florence, Italy in the early 1500's."
            work_of_art.current_location = "La Louvre, Paris"
            work_of_art.materials_used = "Oil Paint on Poplar Wood"
            work_of_art.image_name = "MonaLisa.jpg"
            response_page.art = work_of_art
        elif self.request.get("work") == "Birth-of-Venus":
            response_page.title = "The Birth of Venus"
            work_of_art.artist = "Sandro Botticelli"
            work_of_art.time = "Circa 1485"
            work_of_art.description = "Undoubtedly the most well known and appreciated work of Italy's 15th century, this work follows the theme from Ovid's Metamorphoses."
            work_of_art.current_location = "Uffizi Gallery, Florence"
            work_of_art.materials_used = "Tempera on Canvas"
            work_of_art.image_name = "BirthOfVenus.jpg"
            response_page.art = work_of_art
        self.response.write(response_page.render_view()) # Return the view to the client

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

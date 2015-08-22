#!/usr/bin/env python
# --------------------------
#   pages.py
#   Dynamic Site
#   Friday, 21 August, 2015
#   Alexander Rhett Crammer
#   Full Sail University
# --------------------------
#
class Page(object):
    def __init__(self):
        self._title = None # Title of this page

    def render_view(self):
        ''' Return the view to the client '''
        return open("Pages/Credit.html").read() # Read the template then return it

    # Getters
    @property
    def title(self):
        return self._title

    # Setters
    @title.setter
    def title(self, new_title):
        self._title = new_title

class FamousWorkPage(Page):
    def __init__(self):
        self._art = None # Art objects for the page

    def render_view(self):
        # Render the view with properties local to this object
        return open("Pages/Content.html").read().format(**locals()) # Open the template, read the page to a string, then interpolate this instances' properties and return it

    # Getters
    @property
    def art(self):
        return art

    # Setters
    @art.setter
    def art(self, new_art):
        self._art = new_art

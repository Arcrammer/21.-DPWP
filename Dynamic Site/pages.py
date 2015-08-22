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
        self._view_name = "Welcome" # Name of the view, used for finding the template

    def render_view(self):
        ''' Return the view to the client '''
        self._view = open(str("Pages/{view_name}.html").format(view_name=self._view_name.lower())) # Open the template
        return self._view.read().format(**locals()) # Read the template, interpolate local variables in the data, then return it

    # Getters
    @property
    def title(self):
        return self._title

    @property
    def view_name(self):
        return self._view_name

    # Setters
    @title.setter
    def title(self, new_title):
        self._title = new_title

    @view_name.setter
    def view_name(self, new_view_name):
        self._view_name = new_view_name

class WorkPage(Page):
    def __init__(self):
        self._art = None # Art objects for the page

    # Getters
    @property
    def art(self):
        return art

    # Setters
    @art.setter
    def art(self, new_art):
        self._art = new_art

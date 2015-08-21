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
    def view_name(self):
        return self._view_name

    # Setters
    @view_name.setter
    def view_name(self, new_name):
      self._view_name = new_name

class ContentPage(Page):
    def __init__(self):
        # Polymorphic properties
        self._title = "Content Page"
        self._view_name = "Content"

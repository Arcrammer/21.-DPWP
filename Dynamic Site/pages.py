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
        pass

    def render_view(self):
        return open("Pages/index.html").read().format(**locals()) # Read the template, interpolate local variables in the data, then return it

#!/usr/bin/env python
# --------------------------
#   data.py
#   Dynamic Site
#   Friday, 21 August, 2015
#   Alexander Rhett Crammer
#   Full Sail University
# --------------------------
#
class Work(object):
    # IMPORTANT: There should be five data objects which
    #   should be hard coded in _this_ object. They should
    #   inherit from this object, and they should be 
    #   instantiated within this object, also.
    def __init__(self):
        self._title = None # Title of the work
        self._time = None # String describing the time of the works' completion

class Art(Work):
    def __init__(self):
        self._artist = None # Name of the artist who'd created the work
        self._description = None # Brief explanation of the work
        self._current_location = None # Where the work is currently physically located
        self._materials_used = None # Materials the art was made with, e.g. Wood, Paint, and Stone.
        self._image_path = None # Path to the image

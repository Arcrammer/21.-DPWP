#!/usr/bin/env/python
# --------------------------
#
#   Final Exam
#   Thursday, 27 August, 2015
#   Alexander Rhett Crammer
#   Full Sail University
#
# --------------------------
#
''' Abstract Classes '''

class Place(object):
    '''
    This is an abstract class because it could
    be further separated to more specific
    classes like 'Neighbourhood' or 'State'
    '''
    def __init__(self):
        self._name = None # Name of the place
        self._country = None # Country the place is located in
        self._tempurature = None # Tempurature of the place
        self._habitable = None # Whether the place can be lived in
        self._feeling = None # How it feels there (Beachy and bright, dark and crowded, exotic...)

class Neighbourhood(object):
    '''
    This is a less abstract class because it
    provides data more specific to neighbourhoods
    '''
    def __init__(self):
        self._park_count = None # Amount of parks in the neighbourhood
        self._population = None # Amount of residents
        self._state = None # State of the neighbourhood

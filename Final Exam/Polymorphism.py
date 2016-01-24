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
''' Polymorphism '''

class Food(object):
    def __init__(self):
        self._poisonous = False # Protected properties will be given to child classes
        self._flavour = None # Flavour (bitter, sweet, scorched, sour?)
        self._colour = None # Colour of the food
        self.__native_lands = None # Where the food was discovered
        self.__cost = None # How much the food was purchased for

    def rot(self):
        # TODO: Rot the food
        pass

    def cook(self):
        # TODO: Cook the food
        pass

class RedVelvetCookieDoughBar(Food):
    '''
    This is another subclass. Inheriting from 'Food', objects
    with this class will have all the its' methods and
    properties. We can be more specific here, and we can also
    override some of the methods or properties in 'Food'. This
    overriding is called polymorphism.
    '''
    def __init__(self):
        self._colour = "Red, Brown" # All Spruce trees are of the 'Pinaceae' family, so we can override that property from the superclass
        self._flavour = "Sweet"

    def rot(self):
        '''
        This method was also defined in the 'Food' class, but
        defining it within this class too means we're able to
        perform completely different behaviour as if the
        parent class doesn't even implement this method.
        '''
        # TODO: Rot a specific way differently than other foods
        pass

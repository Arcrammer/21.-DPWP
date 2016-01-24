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
''' Inheritance '''

class Tree(object):
    def __init__(self):
        self._produces_edibles = False # Protected properties will be given to child classes
        self._family = None # Family of the trees' species
        self._genus = None # Genus of the trees' species
        self.__age = 0 # Private properties will not be inherited by subclasses.
        self.__lives = True # Trees die sometimes, right? This is also private so it won't be inheritable

    def grow(self):
        # TODO: Make the tree taller within this method
        pass

    def die(self):
        # TODO: Kill the tree within this method
        pass

class Spruce(Tree):
    '''
    This is a subclass, child class, or inheriting class
    of 'Tree'. To declare a class the child of another
    class just pass the name of your desired superclass
    between the parenthesis after the 'class' keyword.
    
    Now this object has all of the methods and properties
    defined in the 'Tree' class.
    '''
    def __init__(self):
        self._family = "Pinaceae" # All Spruce trees are of the 'Pinaceae' family, so we can override that property from the superclass
        self._genus = "Picea"

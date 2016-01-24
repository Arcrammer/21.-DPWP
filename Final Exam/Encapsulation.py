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
''' Encapsulation '''

class PersonalFinances(object):
    def __init__(self):
        self.credit = "Good" # Public properties are accessible from within the definition of this class, its' children, and from instances of this class
        self._loans_outstanding = None # Protected properties are accessible only within this class definition and the definitions of its' children
        self.__savings_amount = "<< Very Large Number >>" # Private properties are only accessible to this class from within its' definition

    # Getters are virtualised properties which actually execute methods upon call, and they're expected to return values
    @property # This is a decorator and it's used to state that all methods after this line are methods to be executed then return values
    def savings(self): # The name of the method will be the property name. It can differ from the protected variables' name.
        # Do secret stuff before returning a value for the property requested
        return self.__savings_amount # Because the definition of this class has access to '__savings_amount' we're able to return its' value

    # Setters are also virtualised properties but they're called when someone attempts to assign a new value
    @savings.setter # This is a decorator, too, although we rely on the name of the property in the decorators' name instead of the following method
    def savings(self, new_savings_amount): # This method definition will be given a second parameter (the name is ambiguous to you) which contains the new value desired
        # Do secret stuff before setting the new value of the property
        self.__savings_amount = new_savings_amount
        '''
        Because we have access to '__savings_amount'
        within this definition we're able to allow
        the user to set its' value from outside even
        though '__savings_amount' is a private
        property only existing within this class.
        '''
        pass

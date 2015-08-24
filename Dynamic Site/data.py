#!/usr/bin/env python
# --------------------------
#   data.py
#   Dynamic Site
#   Friday, 21 August, 2015
#   Alexander Rhett Crammer
#   Full Sail University
# --------------------------
# MODELS
class Work(object):
    # IMPORTANT: There should be five data objects which
    #   should be hard coded in _this_ object. They should
    #   inherit from this object, and they should be 
    #   instantiated within this object, also.
    def __init__(self):
        self._title = None # Title of the work
        self._time = None # String describing the time of the works' completion
        self._art_name = None # Name of the art object
        self._art = Art() # 'Art' requested

    # Getters
    @property
    def art_name(self):
        return self._art_name

    @property
    def art(self):
        return self._art

    # Setters
    @art_name.setter
    def art_name(self, new_art_name):
        ''' Set the name of the work requested; Set the appropriate properties to self._art '''
        self._art_name = new_art_name
        if self._art_name == "Mona-Lisa":
            self._art._title = self._art_name
            self._art._artist = "Leonardo da Vinci"
            self._art._time = "Early 1500's"
            self._art._description = "Portrait of Lisa Gherardini, wife of Francesco del Giocondo, referred to as Monna Lisa, The Gioconda or The Joconde. Painted in Florence, Italy in the early 1500's."
            self._art._current_location = "La Louvre, Paris"
            self._art._materials_used = "Oil Paint on Poplar Wood"
            self._art._image_name = "MonaLisa.jpg"
        elif self._art_name == "Birth-of-Venus":
            self._art._title = self._art_name
            self._art._artist = "Sandro Botticelli"
            self._art._time = "Circa 1485"
            self._art._description = "Undoubtedly the most well known and appreciated work of Italy's 15th century, this work follows the theme from Ovid's Metamorphoses."
            self._art._current_location = "Uffizi Gallery, Florence"
            self._art._materials_used = "Tempera on Canvas"
            self._art._image_name = "BirthOfVenus.jpg"
        elif self._art_name == "Starry-Night":
            self._art._title = self._art_name
            self._art._artist = "Vincent van Gogh"
            self._art._time = "Circa 1889"
            self._art._description = "Originally titled &quot;La Nuit Entoill&eacute;&quot;, this is pherhaps Van Gogh's most well known rendition of the view from his asylum room at Saint-R&eacute;my-de-Provence."
            self._art._current_location = "Museum of Modern Art, New York"
            self._art._materials_used = "Oil on Canvas"
            self._art._image_name = "StarryNight.jpg"
        elif self._art_name == "Persistence-of-Memory":
            self._art._title = self._art_name
            self._art._artist = "Salvador Dal&#xED;"
            self._art._time = "1931"
            self._art._description = "Dal&#xED; used oil on canvas to portray his perception of softness and hardness. He'd often used ants to resemble death and rotting."
            self._art._current_location = "Museum of Modern Art, New York"
            self._art._materials_used = "Oil on Canvas"
            self._art._image_name = "PresistenceOfMemory.jpg"
        elif self._art_name == "Girl-With-a-Pearl-Earring":
            self._art._title = self._art_name
            self._art._artist = "Johannes Vermeer"
            self._art._time = "1665"
            self._art._description = "Tronie by Johannes Vermeer created 1665."
            self._art._current_location = "Mauritshuis, The Hague"
            self._art._materials_used = "Oil on Canvas"
            self._art._image_name = "GirlWithPearlEarring.jpg"

class Art(Work):
    def __init__(self):
        self._title = None # This should have been inherited?
        self._artist = None # Name of the artist who'd created the work
        self._time = None # Year the work was completed near
        self._description = None # Brief explanation of the work
        self._current_location = None # Where the work is currently physically located
        self._materials_used = None # Materials the art was made with, e.g. Wood, Paint, and Stone.
        self._image_name = None # Path to the image

'''
Alexander Rhett Crammer
Saturday, 8 August, 2015
Design Patterns for Web Programming
Simple Form
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # Instantiate a 'Page' object then
        # return it to the client
        self.response.write(Page().view())

class Page(object):
    def __init__(self):

        # View Template Interpolation Data
        self.page_title = "Simple Form"

        # Read the file 'index.html' then interpolate
        # local variable values with .format(**locals())
        self.template = open('index.html','r').read().format(**locals())

    def view(self):
        # Return the rendered view data
        return self.template

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

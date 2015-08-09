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
        response_page = Page()
        
        if self.request.GET:
          self.form_submission_status = True
          response_page.form_data(self.request.GET)
        else:
          self.form_submission_status = False

        self.response.write(response_page.view(self.form_submission_status))

class Page(object):
    def __init__(self):
        # View Template Interpolation Data
        self.page_title = "Simple Form"

    def view(self, form_submitted):
        # Respond with different elements if the form was submitted
        if form_submitted:
            # Prepare variables for interpolation to the template
            self.full_name = self.form_data['full_name']
            self.payment_method = self.form_data['payment_method']
            self.record = self.form_data['record']
            self.street = self.form_data['street']
            self.city = self.form_data['city']
            self.state = self.form_data['state']
            self.zip_code = self.form_data['zip_code']
            # Read the file 'confirmation.html' then interpolate
            # local variable values with .format(**locals())
            self.template = open('confirmation.html','r').read().format(**locals())
        else:
            # Read the file 'index.html' then interpolate
            # local variable values with .format(**locals())
            self.template = open('index.html','r').read().format(**locals())

        # Return the rendered view data
        return self.template

    def form_data(self, data):
      self.form_data = data

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

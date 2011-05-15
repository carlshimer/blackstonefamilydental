from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import os
from google.appengine.ext.webapp import template

class BsdPage(webapp.RequestHandler):
  def get(self):
      path = os.path.join(os.path.dirname(__file__), 'templates',self.page)
      self.response.out.write(template.render(path,{}))  

class RootPage(BsdPage):
  def __init__(self):
    self.page = 'index.html'

class OfficePage(BsdPage):
  def __init__(self):
    self.page = "theoffice.html"

class LocationPage(BsdPage):
  def __init__(self):
    self.page = "location.html"

class AboutUsPage(BsdPage):
  def __init__(self):
    self.page = "aboutus.html"

application = webapp.WSGIApplication(
          [
  ('/', RootPage),
  ('/theoffice',OfficePage),
  ('/directions',LocationPage),
  ('/aboutus',AboutUsPage),
  ],
          debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()

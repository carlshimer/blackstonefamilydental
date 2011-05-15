from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import os
from google.appengine.ext.webapp import template

class BsdPage(webapp.RequestHandler):
  def get(self):
      path = os.path.join(os.path.dirname(__file__), 'templates',self.page)
      self.response.out.write(template.render(path,{"page":self}))

  def root_class(self):
    return "selected" if self.tab == "home" else ""
  def staff_class(self):
    return "selected" if self.tab == "staff" else ""
  def office_class(self):
    return 'selected' if self.tab == "office" else ""
  def services_class(self):
    return 'selected' if self.tab == "services" else ""
  def before_after_class(self):
    return 'selected' if self.tab == "before_after" else ""
  def newpatient(self):
    return 'selected' if self.tab == "newpatient" else ""

class RootPage(BsdPage):
  def __init__(self):
    self.page = 'index.html'
    self.tab = "home"

class StaffPage(BsdPage):
  def __init__(self):
    self.page = "staff.html"
    self.tab = "staff"

class OfficePage(BsdPage):
  def __init__(self):
    self.page = "theoffice.html"
    self.tab = "office"

class LocationPage(BsdPage):
  def __init__(self):
    self.page = "location.html"

class AboutUsPage(BsdPage):
  def __init__(self):
    self.page = "aboutus.html"


class NewPatientPage(BsdPage):
  def __init__(self):
    self.page = "newpatient.html"
    self.tab = "newpatient"

application = webapp.WSGIApplication(
          [
  ('/', RootPage),
  ('/staff',StaffPage),
  ('/theoffice',OfficePage),
  ('/directions',LocationPage),
  ('/aboutus',AboutUsPage),
  ('/newpatient',NewPatientPage),
  ],
          debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()

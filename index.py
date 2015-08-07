#from google.appengine.ext import webapp
#from google.appengine.ext.webapp.util import run_wsgi_app
import os
from google.appengine.ext.webapp import template
import webapp2

class BsdPage(webapp2.RequestHandler):
  
  def _render(self,page,args):
    path = os.path.join(os.path.dirname(__file__), 'templates',page)
    self.response.out.write(template.render(path,args))
  
  def get(self,*args):
    self._render(self.page,{"page":self})
    
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
  def __init__(self,request=None,response=None):
    self.initialize(request,response)
    self.page = 'index.html'
    self.tab = "home"

class StaffPage(BsdPage):
  def __init__(self,request=None,response=None):
    self.initialize(request,response)
    self.page = "staff.html"
    self.tab = "staff"

class OfficePage(BsdPage):
  def __init__(self,request=None,response=None):
    self.initialize(request,response)
    self.page = "theoffice.html"
    self.tab = "office"

class LocationPage(BsdPage):
  def __init__(self,request=None,response=None):
    self.initialize(request,response)
    self.page = "location.html"

class AboutUsPage(BsdPage):
  def __init__(self,request=None,response=None):
    self.initialize(request,response)
    self.page = "aboutus.html"


class NewPatientPage(BsdPage):
  def __init__(self,request=None,response=None):
    self.initialize(request,response)
    self.page = "newpatient.html"
    self.tab = "newpatient"

    
class ServicesPages(BsdPage):

  def stype(self):
    return self.service_type

  def get(self,service_type):
    self.tab = "services"
    self.service_type = service_type
    self._render("%s.html" % self.service_type,{"page":self})
    
  def selected_rule(self):
    return "#%s { font-weight:bold }" % self.service_type
  
  


                                
class BeforeAfterPage(BsdPage):

  def __init__(self,request=None,response=None):
    self.initialize(request,response)
    self.page = "before_after.html"
    self.tab = "before_after"


                              

    
app = webapp2.WSGIApplication(
  [
    ('/', RootPage),
    ('/staff',StaffPage),
    ('/theoffice',OfficePage),
    ('/directions',LocationPage),
    ('/aboutus',AboutUsPage),
    ('/newpatient',NewPatientPage),
    ('/services/(.*)',ServicesPages),
    ('/before_after',BeforeAfterPage)
    ],
  debug=True)


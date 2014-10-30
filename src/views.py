#coding: utf-8
import sys
import os
from util import write_template

sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))

import json
import logging
import urllib
import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        data = {}
        write_template(self, 'index.html', data)


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
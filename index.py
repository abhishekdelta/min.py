#!/usr/bin/env python
"""
@summary: The brain of min.py 
@author: Abhishek Shrivastava <i.abhi27 [at] gmail [dot] com>

"""
import cgi
import cgitb
import os
import sys

from config   import VALID_PAGES, DEFAULT_PAGE
from render   import render, push_html, error
from urlparse import urlparse

# This is helpful for debugging when enabled. Can remove for production if confident.
cgitb.enable()

# Processing HTTP get/post variables
httpin = {}
storage = cgi.FieldStorage()
for key in storage.keys():
    
    # If its a file upload
    if storage[key].filename is not None:        
        httpin[key+'_name'] = storage[key].filename
        httpin[key+'_type'] = storage[key].type
        httpin[key+'_data'] = storage[key].file.read()
    else:
        httpin[key] = storage.getvalue(key)

# Get page name from URL
page = urlparse(os.environ['REQUEST_URI']).path.lstrip('/')

if page == "": 
    page = DEFAULT_PAGE

# If the URL is like <domain>/hello/123/xyz, then you would want to parse it here.
# and save the URL components into httpin object with proper keys so that controllers
# can make use of it.
if page.startswith('hello'):
    components = page.split("/")
    if len(components) > 1:
        page   = components[0]
        httpin.update({'name' : components[1],
                       'age'  : components[2],
                       'city' : components[3]})

if page not in VALID_PAGES:
    error("Invalid Page - %s!" % page)
    

# Loads the appropriate controller
module = 'controllers.'+page
__import__(module)
controller = sys.modules[module]

# Get the data from the controller
values_dict = controller.output(httpin)

# Render 
push_html(render(page, values_dict))
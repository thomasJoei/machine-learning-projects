import sys, os

# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))
sys.path.append(os.path.dirname(__file__))

# ... build or import your bottle application here ...
# Do NOT use bottle.run() with mod_wsgi

import bottle
from rs import app as application
from bottle import route
import classifier_app
application=bottle.default_app()
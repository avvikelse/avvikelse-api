import os
import sys

os.chdir(os.path.dirname(__file__))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app

# This tells bottle to not catch application specific exceptions instead
# mod_wsgi will handle them and write them to the error_log.
app.catchall = False

application = app

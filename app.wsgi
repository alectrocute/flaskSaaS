import sys, os, logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/Flask-Boilerplate')
os.chdir('/var/www/Flask-Boilerplate')
from run import app
application = app
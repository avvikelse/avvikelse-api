# -*- coding: UTF-8 -*-

from bottle import route, run, debug, Bottle, request, abort
import logging
from mongoengine.connection import connect
from deviation.handlers import deviation_app
import settings as app_settings

logging.basicConfig(level=app_settings.DEBUG, filename=app_settings.LOG_FILENAME)
logger = logging.getLogger(__name__)

debug(app_settings.DEBUG)
connect('deviations')

def dump_email_headers():
    [logger.info("EMAIL: %s" % h) for h in request.headers.values() if '@' in h]

deviation_app.hooks.add('before_request', dump_email_headers)

app = Bottle()
app.mount('/v1/deviations', deviation_app)

@app.route('/')
def root():
    return "Hello TravelHack."

def main():
    run(reloader=True, app=app, host='localhost', port=8888)

if __name__ == "__main__":
    main()


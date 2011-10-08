# -*- coding: UTF-8 -*-

from bottle import route, run, debug, Bottle, request, abort
import logging
from deviation.handlers import deviation_app
import settings as app_settings

logging.basicConfig(level=app_settings.DEBUG, filename=app_settings.LOG_FILENAME)

debug(app_settings.DEBUG)

app = Bottle()
app.mount(deviation_app, '/deviation')

@app.route('/')
def root():
    return "Hello TravelHack."

def main():
    run(reloader=True, app=app, host='localhost', port=8888)

if __name__ == "__main__":
    main()

# -*- coding: UTF-8 -*-
import datetime
from bottle import Bottle, abort

deviation_app = Bottle()

@deviation_app.route('/query/')
def query():
    abort(501)

@deviation_app.route('/:deviation_id/')
def get_deviation( deviation_id):
    return {
        'deviation': {
            'title': 'Stopp vid TCE',
            'description': None,
            'latitude': '18.000',
            'longitude': '58.000',
            'line_number': '4',
            'created_at': str(datetime.datetime.utcnow())
        }
    }

@deviation_app.route('/', method='POST')
def create_update_deviation():
    abort(501)

@deviation_app.route('/', method='PUT')
def update_deviation():
    abort(501)


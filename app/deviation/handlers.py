# -*- coding: UTF-8 -*-
import datetime
from bottle import Bottle, abort

deviation_app = Bottle()

@deviation_app.route('/v:version/query/')
def query(version):
    abort(501)

@deviation_app.route('/v:version/:deviation_id/')
def get_deviation(version, deviation_id):
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

@deviation_app.route('/v:version/', method='POST')
def create_update_deviation(version):
    abort(501)

@deviation_app.route('/v:version/', method='PUT')
def update_deviation(version):
    abort(501)


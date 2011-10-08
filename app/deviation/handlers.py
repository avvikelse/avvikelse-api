# -*- coding: UTF-8 -*-

from bottle import Bottle, abort

deviation_app = Bottle()

@deviation_app.route('/v:version/query/')
def query(version):
    abort(501)

@deviation_app.route('/v:version/:deviation_id')
def get_deviation(version, deviation_id):
    abort(501)

@deviation_app.route('/v:version/', method='POST')
def create_update_deviation(version):
    abort(501)

@deviation_app.route('/v:version/', method='PUT')
def update_deviation(version):
    abort(501)


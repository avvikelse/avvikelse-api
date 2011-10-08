# -*- coding: UTF-8 -*-

from bottle import Bottle, abort

deviation_app = Bottle()

@deviation_app.route('/v:version/query/')
def query(version):
    abort(501)

@deviation_app.route('/v:version/:deviation_id')
def query(version, deviation_id):
    abort(501)

@deviation_app.route('/v:version/', method='POST')
def query(version):
    abort(501)

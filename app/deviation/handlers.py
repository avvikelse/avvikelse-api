# -*- coding: UTF-8 -*-
from datetime import datetime
import logging
from bottle import Bottle, abort, request, response
from deviation.models import Deviation

logger = logging.getLogger(__name__)

deviation_app = Bottle()

@deviation_app.route('/query/')
def query():
    abort(501)

@deviation_app.route('/:deviation_id/')
def get_deviation(deviation_id):
    return {
        'deviation': {
            'id': deviation_id,
            'title': 'Stopp vid TCE',
            'description': None,
            'latitude': '18.000',
            'longitude': '58.000',
            'line_number': '4',
            'created_at': str(datetime.datetime.utcnow())
        }
    }

@deviation_app.route('/:deviation_id/', method='PUT')
def update_deviation(deviation_id):
    abort(501)

@deviation_app.route('/', method='POST')
def create_update_deviation():
    deviation = Deviation()
    deviation.title = request.POST.get('title', None)
    deviation.details = request.POST.get('details', None)

    lat = request.POST.get('latitude', None)
    lng = request.POST.get('longitude', None)
    if lat is not None and lng is not None:
        deviation.location = [lat, lng]

    deviation.scope = request.POST.get('scope', None)
    deviation.route_type = request.POST.get('route_type', None)
    deviation.source = request.POST.get('source', "crowd")

    try:
        deviation.save()
    except Exception, e:
        logger.info('Failed to create deviation %s (%s)' % (e, type(e)))
        response.status = 400
        return {
            'message': 'Could not create deviation.'
        }
    return {
        'id': str(deviation.id)
    }






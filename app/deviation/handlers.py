# -*- coding: UTF-8 -*-
from datetime import datetime, timedelta
import logging
from bottle import Bottle, abort, request, response
from deviation.models import Deviation

logger = logging.getLogger(__name__)

deviation_app = Bottle()

@deviation_app.route('/status/')
def status():
    scope = request.GET.get('scope', None)
    route_type = request.GET.get('route_type', None)
    latitude = request.GET.get('latitude', None)
    longitude = request.GET.get('longitude', None)

    deviation_list = Deviation.objects
    if scope:
        deviation_list.filter(scope=scope)
    if route_type:
        deviation_list.filter(route_type=route_type)
    if latitude is not None and longitude is not None:
        pass

    time_limit = datetime.utcnow() - timedelta(minutes=5)
    deviation_list.filter(created_at__gte=time_limit)

    deviation_list.limit(20)
    deviation_list.order_by('-created_at')

    return {
        'affects': len(deviation_list),
        'comments': [d.comment for d in deviation_list if d.comment is not None]
    }

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
            'created_at': str(datetime.utcnow())
        }
    }

@deviation_app.route('/:deviation_id/', method='PUT')
def update_deviation(deviation_id):
    abort(501)

@deviation_app.route('/', method='POST')
def create_update_deviation():
    deviation = Deviation()
    deviation.comment = request.POST.get('comment', None)

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






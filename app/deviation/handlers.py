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

    deviation = Deviation.objects.get(id=deviation_id)
    return {
        'deviation': {
            'comment': deviation.comment,
            'created_at': deviation.created_at.isoformat(),
            'latitude': '18.000',
            'longitude': '58.000',
            'line': deviation.line,
            'vehicle': deviation.vehicle,
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
        try:
            lat, lng = float(lat), float(lng)
        except ValueError:
            response.status = 400
            return {'message': 'latitude and longitude must be WGS84.'}
        logger.info("lat and lng %s %s" % (lat, lng))
        deviation.location = [float(lat), float(lng)]

    deviation.line = request.POST.get('line', None)
    deviation.vehicle = request.POST.get('vehicle', None)
    deviation.route_type = request.POST.get('transport', None)
    deviation.source = request.POST.get('source', "crowd")

    try:
        deviation.save()
    except Exception, e:
        logger.info('Failed to create deviation %s (%s)' % (e, type(e)))
        response.status = 400
        return {'message': 'Could not create deviation.'}
    return {
        'id': str(deviation.id)
    }






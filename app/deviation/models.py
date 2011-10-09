# -*- coding: UTF-8 -*-
from mongoengine import DateTimeField
from mongoengine.document import Document
from mongoengine.fields import StringField, GeoPointField

class Deviation(Document):
    comment = StringField()
    location = GeoPointField()
    latitude = StringField()
    longitude = StringField()
    transport = StringField()
    stop_point = StringField()
    source = StringField()
    line = StringField()
    vehicle = StringField()
    created_at = DateTimeField()

    meta = {
        'indexes': ['transport', 'line', 'vehicle']
    }

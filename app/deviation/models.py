# -*- coding: UTF-8 -*-
import datetime
from mongoengine import DateTimeField
from mongoengine.document import Document
from mongoengine.fields import StringField, GeoPointField

class Deviation(Document):
    title = StringField()
    details = StringField()
    location = GeoPointField()
    scope = StringField()
    route_type = StringField()
    source = StringField()
    created_at = DateTimeField(default=datetime.datetime.utcnow())

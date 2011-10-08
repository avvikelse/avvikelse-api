# -*- coding: UTF-8 -*-
import datetime
from mongoengine import DateTimeField
from mongoengine.document import Document
from mongoengine.fields import StringField, GeoPointField

class Deviation(Document):
    comment = StringField()
    location = GeoPointField()
    scope = StringField()
    transport = StringField()
    source = StringField()
    line = StringField()
    vehicle = StringField()
    created_at = DateTimeField(default=datetime.datetime.utcnow())

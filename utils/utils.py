#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ConfigParser
import datetime
import os
from decimal import Decimal
from flask import json
from sqlalchemy.ext.declarative import DeclarativeMeta
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


class AlchemyJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                if isinstance(data, unicode):
                    fields[field] = str(data)
                elif isinstance(data, long):
                    fields[field] = data
                elif isinstance(data, int):
                    fields[field] = data
                elif isinstance(data, Decimal):
                    fields[field] = float(data)
                elif isinstance(data, datetime.datetime):
                    fields[field] = data.isoformat()
                elif isinstance(data, datetime.date):
                    fields[field] = data.isoformat()
                elif isinstance(data, datetime.timedelta):
                    fields[field] = (datetime.datetime.min + data).time().isoformat()
                else:
                    fields[field] = None
            return fields

        return json.JSONEncoder.default(self, obj)


class ConfigParserCustomer(ConfigParser.ConfigParser):
    def __init__(self, defaults=None):
        setting_filename = "config"
        profile = ""
        ConfigParser.ConfigParser.__init__(self, defaults=defaults)
        filename = "%s%s.ini" % (setting_filename, profile)
        path = os.path.dirname(os.path.abspath(__file__))
        # path= os.path.abspath(FileName)
        self.read(path + "/" + filename)

    def optionxform(self, option_str):
        return option_str

    def getProperty(self, glo, name, default=""):
        value = self.get(glo, name)
        return default if value is None else value

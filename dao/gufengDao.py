#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import json

from dao import loadSession
from utils.utils import AlchemyJsonEncoder
from table.gufengTable import GufengTable


class GufengDao:
    @staticmethod
    def add(gufengData):
        session = loadSession()
        session.add(gufengData)
        session.commit()
        session.close()

    @staticmethod
    def delete(gufengData):
        session = loadSession()
        session.delete(gufengData)
        session.commit()
        session.close()

    @staticmethod
    def queryByPage(page=1, limit=50):
        session = loadSession()
        queryData = session.query(GufengTable).order_by(GufengTable.update_time).offset((page - 1) * limit).limit(
            limit).all()
        session.close()
        return json.dumps(queryData, cls=AlchemyJsonEncoder)


if __name__ == "__main__":
    gufengData = GufengTable(id=3, name="123", cover="234", link="345", update_desc="456")
    print GufengDao.add(gufengData)
    # queryData = GufengDao.queryByPage()
    # print queryData

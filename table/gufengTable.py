#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, DateTime, DECIMAL, Integer
from dao import Base
import datetime


class GufengTable(Base):
    __tablename__ = "gufeng"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    cover = Column(String(1000))
    link = Column(String(1000))
    update_desc = Column(String(1000))
    update_time = Column(DateTime)

    def __init__(self, id=0, name="", cover="", link="", update_desc="", update_time=datetime.datetime.now()):
        self.id = id
        self.name = name
        self.cover = cover
        self.link = link
        self.update_desc = update_desc
        self.update_time = update_time

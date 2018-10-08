#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, DateTime, DECIMAL, Integer
from sql import Base
import datetime


class BlockTable(Base):
    __tablename__ = "block"

    tid = Column(Integer, nullable=False, primary_key=True)
    _id = Column(String(255))
    id = Column(String(255))
    name = Column(String(255))
    zhName = Column(String(255))
    symbol = Column(String(255))
    change1d = Column(DECIMAL(60, 30))
    price = Column(DECIMAL(60, 30))
    volume_ex = Column(DECIMAL(60, 30))
    marketCap = Column(DECIMAL(60, 30))
    outflow_1w = Column(DECIMAL(60, 30))
    inflow_1w = Column(DECIMAL(60, 30))
    outflow_1d = Column(DECIMAL(60, 30))
    inflow_1d = Column(DECIMAL(60, 30))
    outflow_1h = Column(DECIMAL(60, 30))
    inflow_1h = Column(DECIMAL(60, 30))
    outflow_30m = Column(DECIMAL(60, 30))
    inflow_30m = Column(DECIMAL(60, 30))
    netflow_1w = Column(DECIMAL(60, 30))
    netflow_1h = Column(DECIMAL(60, 30))
    netflow_1d = Column(DECIMAL(60, 30))
    netflow_30m = Column(DECIMAL(60, 30))
    percent_1w = Column(DECIMAL(60, 30))
    percent_1h = Column(DECIMAL(60, 30))
    percent_1d = Column(DECIMAL(60, 30))
    percent_30m = Column(DECIMAL(60, 30))
    main_volume_1w = Column(DECIMAL(60, 30))
    main_volume_1h = Column(DECIMAL(60, 30))
    main_volume_1d = Column(DECIMAL(60, 30))
    main_volume_30m = Column(DECIMAL(60, 30))
    time = Column(DateTime)

    def __init__(self, _id="", id="", name="", zhName="", symbol="", change1d=0, price=0, volume_ex=0,
                 marketCap=0, outflow_1w=0, inflow_1w=0, outflow_1d=0, inflow_1d=0, outflow_1h=0, inflow_1h=0,
                 outflow_30m=0,
                 inflow_30m=0, netflow_1w=0, netflow_1h=0, netflow_1d=0, netflow_30m=0, percent_1w=0, percent_1h=0,
                 percent_1d=0, percent_30m=0, main_volume_1w=0, main_volume_1h=0, main_volume_1d=0,
                 main_volume_30m=0, time=datetime.datetime.utcnow):
        self._id = _id
        self.id = id
        self.name = name
        self.zhName = zhName
        self.symbol = symbol
        self.change1d = change1d
        self.price = price
        self.volume_ex = volume_ex
        self.marketCap = marketCap
        self.outflow_1w = outflow_1w
        self.inflow_1w = inflow_1w
        self.outflow_1d = outflow_1d
        self.inflow_1d = inflow_1d
        self.outflow_1h = outflow_1h
        self.inflow_1h = inflow_1h
        self.outflow_30m = outflow_30m
        self.inflow_30m = inflow_30m
        self.netflow_1w = netflow_1w
        self.netflow_1h = netflow_1h
        self.netflow_1d = netflow_1d
        self.netflow_30m = netflow_30m
        self.percent_1w = percent_1w
        self.percent_1h = percent_1h
        self.percent_1d = percent_1d
        self.percent_30m = percent_30m
        self.main_volume_1w = main_volume_1w
        self.main_volume_1h = main_volume_1h
        self.main_volume_1d = main_volume_1d
        self.main_volume_30m = main_volume_30m
        self.time = time
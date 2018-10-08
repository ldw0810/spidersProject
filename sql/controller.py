#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import json

from blockChain.sql import loadSession
from blockChain.utils.utils import AlchemyJsonEncoder
from mysql import BlockTable


class BlockController:
    @staticmethod
    def add(blockData):
        session = loadSession()
        session.add(blockData)
        session.commit()
        session.close()

    @staticmethod
    def delete(blockData):
        session = loadSession()
        session.delete(blockData)
        session.commit()
        session.close()

    @staticmethod
    def queryAll():
        session = loadSession()
        queryData = session.query(BlockTable).order_by(BlockTable.time).all()
        session.close()
        return json.dumps(queryData, cls=AlchemyJsonEncoder)

    @staticmethod
    def queryByPage(page=1, limit=50):
        session = loadSession()
        queryData = session.query(BlockTable).order_by(BlockTable.time).offset((page - 1) * limit).limit(limit).all()
        session.close()
        return json.dumps(queryData, cls=AlchemyJsonEncoder)

    @staticmethod
    def queryAllSymbol():
        session = loadSession()
        queryData = session.query(BlockTable.symbol).order_by(BlockTable.time).all()
        queryData = {}.fromkeys(["".join(data) for data in queryData]).keys()
        session.close()
        return json.dumps(queryData, cls=AlchemyJsonEncoder)

    @staticmethod
    def queryBySymbol(symbol="BTC", offset=0):
        session = loadSession()
        if offset == 0:
            queryData = session.query(BlockTable).filter(symbol == BlockTable.symbol).order_by(BlockTable.time).all()
        else:
            queryData = session.query(BlockTable).filter(symbol == BlockTable.symbol).offset(offset).order_by(
                BlockTable.time).all()
        session.close()
        return json.dumps(queryData, cls=AlchemyJsonEncoder)

    @staticmethod
    def querySymbolByLimit(page=1, limit=50):
        session = loadSession()
        queryData = session.query(BlockTable).order_by(BlockTable.time).offset((page - 1) * limit).limit(limit).all()
        session.close()
        return json.dumps(queryData, cls=AlchemyJsonEncoder)


if __name__ == "__main__":
    blockController = BlockController()
    queryData = blockController.queryBySymbol("ETH")
    print queryData

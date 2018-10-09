#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import json


class FlaskUtils:

    @staticmethod
    def return_message(error=0, data={}, desc=""):
        return {
            "error": error,
            "data": json.dumps(data),
            "desc": desc or FlaskUtils.get_desc(error)
        }

    @staticmethod
    def get_desc(error):
        error = int(error)
        if isinstance(error, int):
            if error == 0:
                return '成功'
            elif error == 10000:
                return '服务器操作失败'
            elif error == 10001:
                return '传参错误'
        else:
            return ''

if __name__ == '__main__':
    print json.dumps({})
    print '' or 2


#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urlparse

from flask import Flask, render_template, request, jsonify
from dao.gufengDao import GufengDao
from table.gufengTable import GufengTable
from utils.flaskUtils import FlaskUtils

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')


@app.route('/add_gufeng', methods=["POST"])
def add():
    query = urlparse.urlparse(request.url).query
    param_dict = dict([(k, v[0]) for k, v in urlparse.parse_qs(query).items()])
    id = param_dict.get("id")
    name = param_dict.get("name")
    cover = param_dict.get("cover")
    link = param_dict.get("link")
    update_desc = param_dict.get("update_desc")
    update_time = param_dict.get("update_time")
    if id & name & cover & link & update_desc & update_time:
        try:
            gufengData = GufengTable(int(id), name, cover, link, update_desc, update_time)
            GufengDao.add(gufengData)
            return FlaskUtils.return_message()
        except Exception:
            return FlaskUtils.return_message(10001)
    else:
        return FlaskUtils.return_message(10001)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)

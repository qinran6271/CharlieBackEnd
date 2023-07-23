# -*- codeing = utf-8 -*-
from flask import Blueprint, Flask, request, jsonify
from database import date_overviewdb

date_overview = Blueprint('date_overview', __name__)


@date_overview.route('/dateOverview', methods=['GET'])
def overviewfunc():
    data = date_overviewdb.find()
    data = list(data)
    result = []
    keys_to_remove = ['_id']
    for x in data:
        for key in keys_to_remove:
            x.pop(key, None)
        result.append(x)
    return jsonify(result)

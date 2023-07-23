# -*- codeing = utf-8 -*-
from flask import Blueprint, Flask, request, jsonify
from database import datedb

date = Blueprint('date', __name__)


@date.route('/date_details', methods=['GET'])
def datefunc():
    dateIndex = request.args.get('dateIndex')
    query = {
        "dateIndex": dateIndex,
    }
    result = datedb.find_one(query)
    keys_to_remove = ['_id', 'dateIndex']
    for key in keys_to_remove:
        result.pop(key, None)

    return jsonify(result)

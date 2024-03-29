# -*- codeing = utf-8 -*-
from flask import Blueprint, Flask, request, jsonify
# from database import collection
from database import weaving

dream_weaving = Blueprint('dream_weaving', __name__)


@dream_weaving.route('/dreamweaving', methods=['GET'])
def dream():

    # # 获取请求参数
    cardindex = int(request.args.get('cardindex'))
    sessionIndex = int(request.args.get('sessionIndex'))
    currentPage = int(request.args.get('currentPage'))

    query = {
        "cardindex": cardindex,
        "sessionIndex": sessionIndex,
        "currentPage": currentPage,
    }
    result = weaving.find_one(query)
    keys_to_remove = ['_id']
    for key in keys_to_remove:
        result.pop(key, None)

    return jsonify(result)

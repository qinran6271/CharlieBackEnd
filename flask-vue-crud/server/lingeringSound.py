# -*- codeing = utf-8 -*-
from flask import Blueprint, Flask, request, jsonify
# from database import collection
from database import lingering

lingering_sound = Blueprint('lingering_sound', __name__)


@lingering_sound.route('/volumePage', methods=['GET'])
def lingeringSound():

    # # 获取请求参数
    cardindex = int(request.args.get('cardindex'))
    sessionIndex = int(request.args.get('sessionIndex'))

    query = {
        "cardindex": cardindex,
        "sessionIndex": sessionIndex,
    }
    result = lingering.find_one(query)
    keys_to_remove = ['_id', 'cardindex', 'sessionIndex']
    for key in keys_to_remove:
        result.pop(key, None)

    return jsonify(result)


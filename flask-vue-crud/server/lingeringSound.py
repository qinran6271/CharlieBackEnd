# -*- codeing = utf-8 -*-
from flask import Blueprint, Flask, request, jsonify
# from database import collection
from database import lingering

lingering_sound = Blueprint('lingering_sound', __name__)


@lingering_sound.route('/lingeringsound', methods=['GET'])
def lingeringSound():

    # # 获取请求参数
    cardindex = int(request.args.get('cardindex'))
    sessionIndex = int(request.args.get('sessionIndex'))
    videoUrl = request.args.get('videoUrl')

    query = {
        "cardindex": cardindex,
        "sessionIndex": sessionIndex,
        "videoUrl": videoUrl,
    }
    result = lingering.find_one(query)
    keys_to_remove = ['_id']
    for key in keys_to_remove:
        result.pop(key, None)

    return jsonify(result)


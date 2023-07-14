# -*- codeing = utf-8 -*-
from flask import Blueprint, Flask, request, jsonify
# from database import collection
from database import trackdb

track = Blueprint('track', __name__)


@track.route('/tracks', methods=['GET'])
def trackfunc():
    cardindex = int(request.args.get('cardindex'))
    sessionIndex = int(request.args.get('sessionIndex'))
    videoUrl = request.args.get('videoUrl')
    diaorMono = request.args.get('DiaOrMono')

    query = {
        "cardindex": cardindex,
        "sessionIndex": sessionIndex,
        "videoUrl": videoUrl,
        "DiaOrMono": diaorMono
    }
    result = trackdb.find_one(query)
    keys_to_remove = ['_id']
    for key in keys_to_remove:
        result.pop(key, None)

    return jsonify(result)



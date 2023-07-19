# -*- codeing = utf-8 -*-
from flask import Blueprint, Flask, request, jsonify
# from database import collection
from database import rewinddb

rewind = Blueprint('rewind', __name__)


@rewind.route('/rewinds', methods=['GET'])
def rewindfunc():
    # diaorMemory = request.args.get('DiaOrMemory')
    sessionIndex = int(request.args.get('sessionIndex'))

    query = {
        "sessionIndex": sessionIndex,
        # "DiaOrMemory": diaorMemory,
        # "videoUrl": videoUrl,
    }
    result = rewinddb.find_one(query)
    keys_to_remove = ['_id', 'sessionIndex']
    for key in keys_to_remove:
        result.pop(key, None)

    return jsonify(result)


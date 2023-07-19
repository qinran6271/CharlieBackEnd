# -*- codeing = utf-8 -*-
from flask import Blueprint, Flask, request, jsonify
# from database import collection
from database import profiledb

profile = Blueprint('profile', __name__)


@profile.route('/profiledetail', methods=['GET'])
def profilefunc():

    cardindex = int(request.args.get('cardindex'))
    sessionIndex = int(request.args.get('sessionIndex'))


    query = {
        "cardindex": cardindex,
        "sessionIndex": sessionIndex,
    }
    result = profiledb.find_one(query)
    keys_to_remove = ['_id', 'cardindex', 'sessionIndex']
    for key in keys_to_remove:
        result.pop(key, None)

    return jsonify(result)


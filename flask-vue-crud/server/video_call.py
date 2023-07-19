from flask import Blueprint, Flask, request, jsonify
# from database import collection
from database import video_calldb

video_call = Blueprint('video_call', __name__)


@video_call.route('/videocall', methods=['GET'])
def call():
    entry = request.args.get('entry')

    query = {
        "entry": entry
    }

    result = video_calldb.find_one(query)
    keys_to_remove = ['_id', 'entry']
    for key in keys_to_remove:
        result.pop(key, None)

    return jsonify(result)
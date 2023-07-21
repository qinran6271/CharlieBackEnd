from flask import Blueprint, Flask, request, jsonify
# from database import collection
from database import video_calldb

video_call = Blueprint('video_call', __name__)


@video_call.route('/videocall', methods=['GET'])
def call():
    if request.args:
        entry = request.args.get('entry')

        query = {
            "entry": entry
        }

        result = video_calldb.find_one(query)
        keys_to_remove = ['_id', 'entry']
        for key in keys_to_remove:
            result.pop(key, None)

        return jsonify(result)
    else:
        entrys = video_calldb.find()

        data = []
        keys_to_remove = ['_id', "videoLink"]
        for entry in entrys:
            for key in keys_to_remove:
                entry.pop(key, None)
            entry["content"] = entry["content"][0]
            data.append(entry)
        
        result = {"totalNum": len(data), "data": data}
        
        return jsonify(result)
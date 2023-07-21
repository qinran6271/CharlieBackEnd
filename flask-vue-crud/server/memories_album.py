from flask import Blueprint, request, jsonify

from database import memories_album

memories = Blueprint('memories_album', __name__)


@memories.route('/memoriesAlbum', methods=['GET'])
def card():
    if request.args:
        # 处理附带参数的情况
        start_level = request.args.get('start_level')  # 灵犀相册星级：【1星】
        type = request.args.get('type')  # 灵犀相册一段，二段：【一段：default；二段：up】
        name = request.args.get('name')  # 灵犀相册名字：【时与玫瑰】
        query = {
        }
        if not type is None:
            query.update({"type": type})

        if not start_level is None:
            query.update({"start_level": start_level})

        if not name is None:
            query.update({"name": name})

        print(query)
        data = memories_album.find(query)
        data = list(data)
        result = []
        keys_to_remove = ['_id']
        for x in data:
            for key in keys_to_remove:
                x.pop(key, None)
                result.append(x)

        return jsonify(result)

    else:
        data = memories_album.find()
        print(data)
        data = list(data)
        result = []
        keys_to_remove = ['_id']
        for x in data:
            for key in keys_to_remove:
                x.pop(key, None)
                result.append(x)
        return jsonify(result)

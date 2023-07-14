from flask import Blueprint, Flask, request, jsonify
from database import furniture

studio_furniture = Blueprint('furniture', __name__)


@studio_furniture.route('/studio/furniture', methods=['GET'])
def studioFurniture():
    if request.args:
        # 处理附带参数的情况
        type_name = request.args.get('type_name')  # 工作室-家具类型：【画板】
        query = {
            "type_name": type_name,
        }
        data = furniture.find(query)
        data = list(data)
        result = []
        keys_to_remove = ['_id']
        for x in data:
            for key in keys_to_remove:
                x.pop(key, None)
                result.append(x)

        return jsonify(result)

    else:
        data = furniture.find()
        data = list(data)
        result = []
        keys_to_remove = ['_id']
        for x in data:
            for key in keys_to_remove:
                x.pop(key, None)
            result.append(x)
        return jsonify(result)



from flask import Blueprint, Flask, request, jsonify
from database import furniture

studio_furniture = Blueprint('furniture', __name__)


@studio_furniture.route('/studio/furniture', methods=['GET'])
def studioFurniture():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '成功', 'result': None}

    data = furniture.find()
    data = list(data)
    result = []
    keys_to_remove = ['_id', 'name', 'detail', 'materials', 'memory', 'type', 'type_name', 'file_path']
    for x in data:
        for key in keys_to_remove:
            x.pop(key, None)
        result.append(x)
    return jsonify(result)

    
   
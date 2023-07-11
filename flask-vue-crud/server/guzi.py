from flask import Blueprint, Flask, request, jsonify
from database import guzi

merch = Blueprint('guzi', __name__)


@merch.route('/guzi', methods=['GET'])
def merchandise():

    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '成功', 'result': None}



    data = guzi.find()
    data = list(data)
    result = []
    keys_to_remove = ['_id', 'release_time', 'series', 'name', 'type', 'price', 'access', 'size', 'texture', 'craft', 'file_path']
    for x in data:
        for key in keys_to_remove:
            x.pop(key, None)
            result.append(x)
    return jsonify(result)

    
   
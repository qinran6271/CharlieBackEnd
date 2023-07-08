# -*- codeing = utf-8 -*-
from flask import Blueprint, Flask, request, jsonify
# from database import collection
from database import weaving

dream_weaving = Blueprint('dream_weaving', __name__)


@dream_weaving.route('/dreamweaving', methods=['GET'])
def dream():

    # # 获取请求参数
    chap_name = request.args.get('chap_name')
    subchap_name = request.args.get('subchap_name')
    totalNum = int(request.args.get('totalNum'))
    num = int(request.args.get('num'))
    type = request.args.get('type')
    content = request.args.get('content')

    query = {
        "chap_name": chap_name,
        "subchap_name": subchap_name,
        "totalNum": totalNum,
        "num": num,
        "type": type,
        "content": content
    }
    result = dream_weaving.find_one(query)
    keys_to_remove = ['_id', 'chap_name', 'subchap_name', 'totalNum', 'num', 'type', 'content']
    for key in keys_to_remove:
        result.pop(key, None)

    return jsonify(result)

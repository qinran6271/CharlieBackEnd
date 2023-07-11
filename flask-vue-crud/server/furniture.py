from flask import Blueprint, Flask, request, jsonify
from database import furniture

furniture = Blueprint('furniture', __name__)


@furniture.route('/furniture', methods=['GET'])
def furniture():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '成功', 'result': None}

    result = furniture.find()

    return jsonify(result)

    
   
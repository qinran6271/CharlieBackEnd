from flask import Blueprint, Flask, request, jsonify
from database import guzi

guzi = Blueprint('guzi', __name__)


@guzi.route('/guzi', methods=['GET'])
def guzi():

    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '成功', 'result': None}

    result = guzi.find()
    
    return jsonify(result)

    
   
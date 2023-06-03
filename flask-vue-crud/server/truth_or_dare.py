from flask import Blueprint, Flask, request, jsonify
# from database import collection
from database import truth_dare

truth_or_dare = Blueprint('truth_or_dare', __name__)


@truth_or_dare.route('/truthordare', methods=['GET'])
def truth():

    # 以下是真心话内容
    # # 获取请求参数
    # data_type = request.args.get('type')
    # person = request.args.get('person')
    # num = int(request.args.get('num'))
    # y_or_n = request.args.get('yOrN')

    # 构建查询参数
    # query = {
    #     "type": data_type,
    #     "person": person,
    #     "num": num,
    #     "yOrN": y_or_n
    # }
    # result = truth_dare.find_one(query)
    # keys_to_remove = ['_id', 'type', 'person', 'num', 'yOrN']
    # for key in keys_to_remove:
    #     result.pop(key, None)
    
    # return jsonify(result)

    # 以下是测试，可删除
    query = {
        "type": "真心话",
        "person": "我",
        "num": 11,
        "yOrN": "NO"
    }

    result = truth_dare.find_one(query)
    keys_to_remove = ['_id', 'type', 'person', 'num', 'yOrN']
    for key in keys_to_remove:
        result.pop(key, None)
    # result.pop('_id', None)
    print(result)
    return jsonify(result)
    
   
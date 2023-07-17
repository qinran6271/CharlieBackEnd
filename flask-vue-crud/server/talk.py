from flask import Blueprint, Flask, request, jsonify
from database import talk_coll
import json

talk= Blueprint('talk', __name__)
@talk.route('/talk', methods=['GET'])
def talkFunc():
    if request.args:
        # 处理附带参数的情况
        name = request.args.get('name') # 闲聊名称

        query = {
            "talk_name" : name
        }
        data = talk_coll.find_one(query)
        keys_to_remove = ['_id','talk_name']
        for key in keys_to_remove:
            data.pop(key, None)

        return jsonify(data)


    else:
        # 只发送GET请求但没有参数的情况的响应
        data = talk_coll.find()
        data = list(data)
        result = []
        keys_to_remove = ['_id','talk_content']
        
        for x in data:
            result.append(x["talk_name"])
        return jsonify(result)
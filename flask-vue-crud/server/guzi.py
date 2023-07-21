from flask import Blueprint, request, jsonify

from database import guzi

merch = Blueprint('guzi', __name__)


@merch.route('/guzi', methods=['GET'])
def merchandise():
    if request.args:
        # 处理附带参数的情况
        type = request.args.get('type')  # 谷子类型：【徽章】
        name = request.args.get('name')  # 谷子名字：【满赠透卡】
        sign = request.args.get('sign')  # 谷子名字：【满赠透卡
        query = {
        }
        if not type is None:
            query.update({"type": type})

        if not name is None:
            condition = {}
            condition['$regex'] = name
            query.update({"name": condition})

        if not sign is None:
            print(sign)
            if sign == "priceASC":
                data = guzi.find(query).sort("price", 1)
            if sign == "priceDESC":
                data = guzi.find(query).sort("price", -1)
            if sign == "timeASC":
                data = guzi.find(query).sort("release_time", 1)
            if sign == "timeDESC":
                data = guzi.find(query).sort("release_time", -1)
        else:
            data = guzi.find(query)
        data = list(data)
        # print(data)
        result = []
        keys_to_remove = ['_id']
        for x in data:
            for key in keys_to_remove:
                x.pop(key, None)
                result.append(x)

        return jsonify(result)

    else:
        data = guzi.find()
        data = list(data)
        # print(data)
        result = []
        keys_to_remove = ['_id']
        for x in data:
            for key in keys_to_remove:
                x.pop(key, None)
                result.append(x)
        return jsonify(result)

    
   
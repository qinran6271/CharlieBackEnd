from flask import Blueprint, Flask, request, jsonify
# from database import chapters
# from database import sub_chapters

day_and_night = Blueprint('day_and_night', __name__)

@day_and_night.route('/dayandnight', methods=['GET'])
def dayNight():
    # if request.args:
    #     # 处理附带参数的情况
    #     chap = request.args.get('chap') # 章节数
    #     subchap = request.args.get('subchap') # “章节数-小节数”

    #     query = {
    #         "subchap_name": subchap,
    #     }
    #     data = sub_chapters.find_one(query)
    #     keys_to_remove = ['_id','subchap_type','subchap_name']
    #     for key in keys_to_remove:
    #         data.pop(key, None)

    #     chap_data =  chapters.find_one({'chap_num':chap})
    #     data['chap_title'] = chap_data['name']
        # data['videoUrl'] = chap_data['video']

    #     return jsonify(data)


    # else:
    #     # 只发送GET请求但没有参数的情况的响应
    #     data = chapters.find()
    #     keys_to_remove = ['_id','name','intro','behind','image','behind']
    #     for key in keys_to_remove:
    #         data.pop(key, None)
    #     return jsonify(data)
    return "hi"

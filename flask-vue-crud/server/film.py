from database import film_chaps_coll
from database import film_cards_coll
from flask import Blueprint, Flask, request, jsonify
import json

film= Blueprint('film', __name__)
@film.route('/film', methods=['GET'])
def filmFunc():
    
    sessionIndex = int(request.args.get('sessionIndex'))
    
    # # 构建查询参数
    query = {
        "chap_num": sessionIndex + 1,
    }

    result = film_chaps_coll.find_one(query)
    keys_to_remove = ['_id', 'card_name', 'chap_name', 'chap_num','total_num', 'part']
    for key in keys_to_remove:
        result.pop(key, None)
    
    return jsonify(result)
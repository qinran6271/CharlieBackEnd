from flask import Blueprint, Flask, request, jsonify
from database import chat_calls, chat_overview, chat_details
import json

chat= Blueprint('chat', __name__)
@chat.route('/chat', methods=['GET'])
def chatFunc():
    if 'type' in request.args:
        chat_type = request.args.get('type')
        query = {
            "type": chat_type,
        }
        result = chat_overview.find_one(query)
        keys_to_remove = ['_id']
        for key in keys_to_remove:
            result.pop(key, None)
        
        return jsonify(result)

    elif 'indexcode' in request.args:
        chat_type = request.args.get('indexcode')
        query = {
            "indexCode": chat_type,
        }
        result = chat_details.find_one(query)
        keys_to_remove = ['_id','indexCode']
        for key in keys_to_remove:
            result.pop(key, None)
        
        return jsonify(result)
    
    elif 'callcode' in request.args:
        chat_type = request.args.get('callcode')
        query = {
            "callCode": chat_type,
        }
        result = chat_calls.find_one(query)
        keys_to_remove = ['_id','callCode']
        for key in keys_to_remove:
            result.pop(key, None)
        
        return jsonify(result)

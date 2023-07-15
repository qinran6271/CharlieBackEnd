from flask import Blueprint, Flask, request, jsonify
from database import moments_details, moments_overview
import json

moments = Blueprint('moments', __name__)
@moments.route('/moments', methods=['GET'])
def momentsFunc():
    if 'type' in request.args:
        moments_type = request.args.get('type')
        query = {
            "type": moments_type,
        }
        result = moments_overview.find_one(query)
        keys_to_remove = ['_id']
        for key in keys_to_remove:
            result.pop(key, None)
        
        return jsonify(result)

    elif 'indexcode' in request.args:
        indexcode = request.args.get('indexcode')
        query = {
            "indexCode": indexcode,
        }
        result = moments_details.find_one(query)
        keys_to_remove = ['_id','indexCode']
        for key in keys_to_remove:
            result.pop(key, None)
        
        return jsonify(result)
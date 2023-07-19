from flask import Blueprint, Flask, request, jsonify
from database import characters_collection
import json

characters= Blueprint('characters', __name__)
@characters.route('/characters', methods=['GET'])
def charFunc():
    
    char_name = request.args.get('name')
    query = {
        "name": char_name,
    }
    result = characters_collection.find_one(query)
    keys_to_remove = ['_id']
    for key in keys_to_remove:
        result.pop(key, None)
    
    return jsonify(result)
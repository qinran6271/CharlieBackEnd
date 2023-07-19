from database import details
from flask import Blueprint, Flask, request, jsonify
import json

charlie_details= Blueprint('charlie_details', __name__)
@charlie_details.route('/charlie_details', methods=['GET'])
def detailsFunc():
    
    data = details.find()
    data = list(data)
    result = []

    keys_to_remove = ['_id']
    for x in data:
        for key in keys_to_remove:
            x.pop(key, None)
        result.append(x)

    return jsonify(result)
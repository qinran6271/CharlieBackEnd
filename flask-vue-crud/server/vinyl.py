from flask import Blueprint, Flask, request, jsonify
from database import vinyl_collection

vinyl = Blueprint('vinyl', __name__)


@vinyl.route('/vinyl', methods=['GET'])
def vinylFunc():

    data = vinyl_collection.find()
    data = list(data)
    print(data)
    result = []
    keys_to_remove = ['_id']
    for x in data:
        for key in keys_to_remove:
            x.pop(key, None)
        result.append(x)
    return jsonify(result)   
    

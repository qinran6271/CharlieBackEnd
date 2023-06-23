from flask import Blueprint, Flask, request, jsonify

day_and_night = Blueprint('day_and_night', __name__)

@day_and_night.route('/dayandnight', methods=['GET'])
def ggg():
    return "hi"
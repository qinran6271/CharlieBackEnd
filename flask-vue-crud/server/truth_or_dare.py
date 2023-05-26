from flask import Blueprint
from database import collection

truth_or_dare = Blueprint('truth_or_dare', __name__)


@truth_or_dare.route('/', methods=['GET'])
def index():
    
    document = collection.find()[1]


    return document['para'][0]["content"]
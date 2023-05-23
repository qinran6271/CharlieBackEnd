from flask import Flask
import json
from database import collection


app = Flask(__name__)

@app.route('/')
def index():
    
    document = collection.find()[1]


    return document['para'][0]["content"]


if __name__ == '__main__':
    app.run()
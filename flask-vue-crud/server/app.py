from flask import Flask
from flask_cors import CORS
from truth_or_dare import truth_or_dare


app = Flask(__name__)
app.register_blueprint(truth_or_dare)

# @app.route('/')
# def index():
    
#     document = collection.find()[1]


#     return document['para'][0]["content"]

CORS(app)
if __name__ == '__main__':
    app.run()
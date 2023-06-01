from flask import Flask, render_template, send_from_directory
from flask_cors import CORS
from flask_compress import Compress
from truth_or_dare import truth_or_dare
import requests


# app = Flask(__name__)
app = Flask(__name__,
            static_folder = "../charlieComUI/dist",
            )
CORS(app)
# 启用 Gzip 压缩
app.config["COMPRESS_REGISTER"] = False  # disable default compression of all eligible requests
compress = Compress()
compress.init_app(app)
# app.config['COMPRESS_MIMETYPES'] = ['text/html', 'text/css', 'text/javascript', 'application/javascript']
# app.config['COMPRESS_LEVEL'] = 6
# app.config['COMPRESS_MIN_SIZE'] = 500

    
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    print(filename)
    return send_from_directory(app.static_folder, filename)

# @app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        # return requests.get('http://localhost:8080/{}'.format(path)).text
        return send_from_directory(app.static_folder, 'index.html')


app.register_blueprint(truth_or_dare)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
from flask import Flask, render_template, send_from_directory
from flask_cors import CORS
from flask_compress import Compress
from truth_or_dare import truth_or_dare
from day_and_night import day_and_night
from dream_weaving import dream_weaving
import requests
# form CharlieBackEnd.server
from guzi import merch
from studio_furniture import studio_furniture
# from memories_album import memories
from rewind import rewind
from lingeringSound import lingering_sound
from profile import profile
from track import track
from chat import chat
from moments import moments
from vinyl import vinyl
from characters import characters
from talk import talk
from charlie_details import charlie_details
from film import film

# 路径可能需要更改, 到时候使用前端的dist文件
app = Flask(__name__,
            static_folder = "../dist/static",
            template_folder = "../dist"
            )

CORS(app)
# 启用 Gzip 压缩
app.config["COMPRESS_REGISTER"] = False  # disable default compression of all eligible requests
compress = Compress()
compress.init_app(app)
# app.config['COMPRESS_MIMETYPES'] = ['text/html', 'text/css', 'text/javascript', 'application/javascript']
# app.config['COMPRESS_LEVEL'] = 6
# app.config['COMPRESS_MIN_SIZE'] = 500

    
# 打开静态文件（不一定有用先保留）
# @app.route('/')
# def index():
#     # return send_from_directory(app.static_folder, 'index.html')
#     return render_template('../../../charlieComUI/dist2/index.html')

# @app.route('/<path:filename>')
# def serve_static(filename):
#     print(filename)
#     return send_from_directory(app.static_folder, filename)


# for history mode （放服务器的话去要配合dockerfile，还没改）
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')
#     if app.debug:
#         # return requests.get('http://43.154.208.135/{}'.format(path)).text



app.register_blueprint(truth_or_dare)
app.register_blueprint(day_and_night)
app.register_blueprint(dream_weaving)
app.register_blueprint(merch)
app.register_blueprint(studio_furniture)
#app.register_blueprint(memories)

app.register_blueprint(rewind)
app.register_blueprint(lingering_sound)
app.register_blueprint(track)
app.register_blueprint(profile)
app.register_blueprint(chat)
app.register_blueprint(moments)
app.register_blueprint(vinyl)
app.register_blueprint(characters)
app.register_blueprint(talk)
app.register_blueprint(charlie_details)
app.register_blueprint(film)

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=5000)
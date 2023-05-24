# CharlieBackEnd

cd flask-vue-crud

cd server

source env/bin/activate

(pip install Flask==2.2.3 Flask-Cors==3.0.10 )

FLASK_APP=app.py flask run 或 flask run


# database

(pip3 install pymongo[srv])

添加config.py，复制config_template.py到config.py里，并将ENCRYPTED_MONGODB_URL后引号部分修改
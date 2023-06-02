import datetime
from flask import Flask

from common import framwork
from app.urls import init_official


def create_app():
    app = Flask(__name__, static_folder='../static', static_url_path="", template_folder='../templates')
    app.secret_key = '123456'
    app.config['JSON_AS_ASCII'] = False
    app.permanent_session_lifetime = datetime.timedelta(days=1)
    framwork.init(app)
    init_official(app)
    return app

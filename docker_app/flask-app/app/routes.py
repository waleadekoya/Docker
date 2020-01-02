from flask import Blueprint

import os

home = Blueprint('home', __name__)


@home.route('/')
def home_page():
    app_name = os.getenv('APP_NAME')
    msg = "Hello from {} running in a Docker container served by uwsgi web server!".format(app_name)
    return 'Flask Web App Home Page' if not app_name else msg

from flask import Flask
from biblioteca-back.ext import configuration
from .views import root


def create_app():
    app = Flask(__name__)
    configuration.init_app(app)

    app.add_url_rule('/', view_func=root)

    return app
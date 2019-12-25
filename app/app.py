# -*- coding: utf-8 -*- 
# @Time : 2019/12/25 21:59 
# @Author : wuson
# @File : app.py

from flask import Flask

def register_blueprints(app):
    from app.api.v1 import create_blueprint_v1

    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')

    register_blueprints(app)

    return app

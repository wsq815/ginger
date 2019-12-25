# -*- coding: utf-8 -*- 
# @Time : 2019/12/25 21:59 
# @Author : wuson
# @File : app.py

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    return app

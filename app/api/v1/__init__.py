# -*- coding: utf-8 -*- 
# @Time : 2019/12/25 22:31 
# @Author : wuson
# @File : __init__.py.py
from flask import Blueprint
from app.api.v1 import user, book

def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)

    user.api.register(bp_v1, url_prefix='/user')
    book.api.register(bp_v1, url_prefix='/book')
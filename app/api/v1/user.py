# -*- coding: utf-8 -*- 
# @Time : 2019/12/25 22:32 
# @Author : wuson
# @File : user.py
from flask import Blueprint

user = Blueprint('user', __name__)

@user.route('/v1/user/get')
def get_user():
    return 'i am wuson'
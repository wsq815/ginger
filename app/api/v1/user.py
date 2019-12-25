# -*- coding: utf-8 -*- 
# @Time : 2019/12/25 22:32 
# @Author : wuson
# @File : user.py

from app.libs.redprint import Redprint


api = Redprint('user')

@api.route('/get')
def get_user():
    return 'i am wuson'
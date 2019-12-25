# -*- coding: utf-8 -*- 
# @Time : 2019/12/25 22:32 
# @Author : wuson
# @File : book.py

from app.libs.redprint import Redprint

api = Redprint('book')

@api.route('/get')
def get_book():
    return 'get book'

@api.route('/create')
def create_book():
    return 'create book'
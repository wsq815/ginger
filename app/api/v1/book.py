# -*- coding: utf-8 -*- 
# @Time : 2019/12/25 22:32 
# @Author : wuson
# @File : book.py
from flask import Blueprint

book = Blueprint('book', __name__)

@book.route('/v1/book/get')
def get_book():
    return 'get book'
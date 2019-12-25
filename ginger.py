# -*- coding: utf-8 -*- 
# @Time : 2019/12/25 21:58 
# @Author : wuson
# @File : ginger.py
from app.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
import os
import sys

from sayhello import app

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'   #使用sqlite作为数据库引擎
else:
    prefix = 'sqlite:////'


dev_db = prefix + os.path.join(os.path.dirname(app.root_path), 'data.db') #设置URI

SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')  #设置密钥
SQLALCHEMY_TRACK_MODIFICATIONS = False   #关闭警告消息
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)   #设置URI

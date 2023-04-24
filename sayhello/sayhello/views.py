# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
from flask import flash, redirect, url_for, render_template

from sayhello import app, db
from sayhello.forms import HelloForm
from sayhello.models import Message


@app.route('/', methods=['GET', 'POST'])
def index():
    form = HelloForm() #实例化表单类
    if form.validate_on_submit(): #验证表单
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message) #添加记录到数据库会话
        db.session.commit() #提交会话
        flash('成功留言')
        return redirect(url_for('index'))

    messages = Message.query.order_by(Message.timestamp.desc()).all() #对留言进行降序排序
    return render_template('index.html', form=form, messages=messages)

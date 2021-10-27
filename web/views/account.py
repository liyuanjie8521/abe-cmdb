#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   account.py
@Time    :   2021/09/30 15:07:53
@Author  :   Elliot Li yuanjie
@Version :   1.0
@Contact :   liyuanjie8521@163.com
@License :   (C)Copyright 2020-2021, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
"""
用户账户相关功能: 注册,登录,注销
"""
from django.shortcuts import render,HttpResponse,redirect
from web.forms.account import RegisterModelForm,LoginForm
from django.conf import settings
from django.http import JsonResponse
from web import models
from django.contrib.auth.models import User, Group

import uuid
import datetime

def register(request):
    """ 注册　"""
    if request.method == 'GET':
        form = RegisterModelForm()
        return render(request,'register.html',{'form': form})
    #print(request.POST)
    form = RegisterModelForm(data=request.POST)
    if form.is_valid():
        #print(form.cleaned_data)
        # 验证通过,写入数据库,优点:入库前会自动剔除无用数据(重复密码和验证码等字段,密码要是密文)
        # instance = form.save 在数据库中新增一条数据,并将新增的这条数据赋值给instance

        # 用户表中新建一条数据(注册)
        instance = form.save()

        return JsonResponse({'status': True,'data': '/web/login/'})
    return JsonResponse({'status': False,'error': form.errors})


def login(request):
    """ 用户名和密码登录 """
    if request.method == 'GET':
        form = LoginForm(request)
        return render(request,'login.html',{'form': form})
    form = LoginForm(request,data=request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        #user_object = models.UserInfo.objects.filter(username=username,password=password).first()
        # (手机=username and pwd=pwd) or (邮箱=username and pwd=pwd)
        from django.db.models import Q
        user_object = models.UserInfo.objects.filter(Q(username=username) | Q(email=username)).filter(password=password).first()
        if user_object:
            # 登录成功为止
            request.session['user_id'] = user_object.id
            request.session.set_expiry(60 * 60 * 24 * 14)
            return redirect('/web/index')
        form.add_error('username','用户名或密码错误')
    return render(request,'login.html',{'form': form})


def logout(request):
    request.session.flush()
    return redirect('/web/index')

def add_ldap_users(request):
    return render("account/list_users.html", request, {})

def sync_ldap_users_groups(request):
    return render("account/list_users.html", request, {})
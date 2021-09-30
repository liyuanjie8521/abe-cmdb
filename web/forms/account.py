from django import forms
from web import models
from web.forms.bootstrap import BootStrapForm
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

from django.conf import settings
import random

from utils import encrypt

class RegisterModelForm(BootStrapForm,forms.ModelForm):

    password = forms.CharField(
        label='密码',
        min_length=8,
        max_length=30,
        error_messages = {
            'min_length': "密码长度不能小于8个字符",
            'max_length': "密码长度不能大于30个字符"
        },
        widget=forms.PasswordInput()
    )
    confirm_password = forms.CharField(
        label='重复密码',
        min_length=8,
        max_length=30,
        error_messages = {
            'min_length': "重复密码长度不能小于8个字符",
            'max_length': "重复密码长度不能大于30个字符"
        },
        widget=forms.PasswordInput()
    )

    class Meta:
        model = models.UserInfo
        #fields = "__all__"
        fields = ["username","email","password","confirm_password"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = "请输入{}".format(field.label,)

    def clean_username(self):
        username = self.cleaned_data['username']

        exists = models.UserInfo.objects.filter(username=username).exists()
        if exists:
            raise ValidationError('用户名已存在')
            #self.add_error('username',"用户名已存在")

        return username


    def clean_email(self):
        email = self.cleaned_data['email']
        exists = models.UserInfo.objects.filter(email=email).exists()
        if exists:
            raise ValidationError('邮箱已存在')

        return email

    def clean_password(self):
        pwd = self.cleaned_data['password']
        # 加密返回
        return encrypt.md5(pwd)

    def clean_confirm_password(self):

        pwd = self.cleaned_data.get('password')
        confirm_pwd = encrypt.md5(self.cleaned_data['confirm_password'])
        if pwd != confirm_pwd:
            raise ValidationError('两次密码不一致')
        return confirm_pwd

class LoginForm(BootStrapForm,forms.Form):
    username = forms.CharField(label='用户名或邮箱')
    password = forms.CharField(label='密码',widget=forms.PasswordInput(render_value=True))

    def __init__(self,request,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.request = request

    def clean_password(self):
        pwd = self.cleaned_data['password']
        # 加密 & 返回
        return encrypt.md5(pwd)

# Here are the modules and libraries referenced by the script.
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from web import models
# Here is the content code for the script.

class AuthMiddleware(MiddlewareMixin):

    def process_request(self,request):
        """ 如果用户已登录,则request中赋值 """
        user_id = request.session.get('user_id',0)
        user_object = models.UserInfo.objects.filter(id=user_id).first()
        request.tracer = user_object

        # 白名单: 没有登录都可以访问的URL.
        """
        1.　获取当前用户访问的URL
        2. 检查URL是否在白名单中,如果再则可以继续向后访问,如果不在则进行判断是否已登录.
        """
        if request.path_info settings.WHITE_REGEX_URL_LIST:
            return
        # 检查用户是否已登录,已登录继续往后走,未登录则返回登录页面
        if request.tracer:
            return redirect('login')
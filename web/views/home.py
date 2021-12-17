from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/web/login')
def index(request):
    return render(request,'index.html')

#5、home页面：只有登录才返回，否则返回到login页面
@login_required(login_url='/web/login')
def home(request):
    return redirect('/web/index')
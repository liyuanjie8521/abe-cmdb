from django.conf.urls import url,include
from web.views import account
from web.views import home

urlpatterns = [
   url(r'^register/$',account.register,name='register'),
   url(r'^login/$',account.Login.as_view(),name='login'),
   url(r'^home/$',home.home,name='home'),
   # url(r'^login/$',account.login,name='login'),
   url(r'^index/$',home.index,name='index'),
   url(r'^logout/$',account.logout,name='logout'),
]
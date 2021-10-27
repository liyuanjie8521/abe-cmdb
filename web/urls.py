from django.conf.urls import url,include
from web.views import account
from web.views import home

urlpatterns = [
   url(r'^register/$',account.register,name='register'),
   url(r'^login/$',account.login,name='login'),
   url(r'^index/$',home.index,name='index'),
   url(r'^logout/$',account.logout,name='logout'),
   url(r'^users/add_ldap_users$', account.add_ldap_users,name='add_ldap_users'),
   url(r'^users/sync_ldap_users_groups$',account.sync_ldap_users_groups,name='sync_ldap_users_groups'),
]
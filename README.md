# AbeCmdb

## 介绍
基于Ansible开发的Cmdb资产管理系统

### 1. 用户单点登录和统一认证

1. 支持普通用户注册和登录
2. 支持通过ldap认证来登录

#### 1.1 LDAP用户验证原理

1. 每个用户在LDAP系统中有一个唯一的DN值. 例如: uid=liyuanjie,ou=django,dc=yuan,dc=com
2. 其中: yuan.com是域名, django是组名,liyuanjie是用户名. 用cn和uid都可以生成DN.
3. django-auth-ldap模块都是用DN来验证用户和获取用户信息的.
4. django-auth-ldap模块有2种方式获取用户DN:
   - 用户DN模板: 使用AUTH_LDAP_USER_DN_TEMPLATE提供的模板生成DN
   - 使用AUTH_LDAP_GROUP_SEARCH,django-auth-ldap会使用AUTH_LDAP_BIND_DN和AUTH_LDAP_BIND_PASSWORD提供的dn与密码根据AUTH_LDAP_GROUP_SEARCH提供的查询条件去查找用户名,查不到,验证失败,查到用户,就使用返回的数据生成用户的DN.

#### 1.2 ldap模块报错处理

1. 安装django-auth-ldap报错
```shell
  ERROR: Failed building wheel for python-ldap
Failed to build python-ldap
ERROR: Could not build wheels for python-ldap which use PEP 517 and cannot be installed directly
```
处理方法:
```shell
pip install --upgrade pip setuptools wheel
```
ubuntu18.04 Linux系统安装gcc环境
```shell
sudo apt-get -y install build-essential
```
报错:
```shell
  Modules/common.h:15:10: fatal error: lber.h: No such file or directory
   #include <lber.h>
            ^~~~~~~~
  compilation terminated.
  error: command 'gcc' failed with exit status 1
  ----------------------------------------
  ERROR: Failed building wheel for python-ldap
Failed to build python-ldap
ERROR: Could not build wheels for python-ldap, which is required to install pyproject.toml-based projects
```
安装:
```shell
sudo apt-get install libsasl2-dev python-dev libldap2-dev libssl-dev
sudo apt-get install -y python-dev libldap2-dev libsasl2-dev libssl-dev
sudo yum install python-devel
sudo yum install openldap-devel
```
再执行安装django-auth-ldap模块的操作:
```shell
pip --no-cache-dir install django-auth-ldap
```

### 参考帮助

1. django-auth-ldap配置方法: https://pypi.org/project/django-auth-ldap/3.0.0/
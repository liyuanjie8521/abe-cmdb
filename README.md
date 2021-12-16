# AbeCmdb

## 介绍
基于Ansible开发的Cmdb资产管理系统

### 用户单点登录和统一认证

1. 支持普通用户注册和登录
2. 支持通过ldap认证来登录



### 报错处理

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

1. ldap配置方法: https://pypi.org/project/django-ldap/
2. django配置ldap认证: https://www.cnblogs.com/jiaxinzhu/p/12571891.html
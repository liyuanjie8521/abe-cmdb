#!/bin/sh
# set -x
log() {
    local prefix="[$(date +%Y/%m/%d\ %H:%M:%S)]: "
    echo "${prefix} $@" >&2
}

export LESSCHARSET=utf-8

SYSTEM=`uname -s`
echo "当前操作系统为$SYSTEM, 设置换行符"
if [[ $SYSTEM =~ "MINGW" ]]
then
  git config --global core.autocrlf false # windows执行
else
  git config --global core.autocrlf input # mac执行
fi

log "INFO" "设置长路径与大小写敏感"
git config --global core.longpaths true
git config --global core.ignorecase false

log "INFO" "设置UTF-8解决中文乱码"
git config --global credential.helper store
git config --global i18n.commitencoding utf-8
git config --global i18n.logoutputencoding utf-8
git config --global core.quotepath false
git config --global gui.encoding utf-8

SYSTEM=`uname -s`
log "INFO" "当前操作系统为$SYSTEM, 设置换行符"
if [[ $SYSTEM =~ "MINGW" ]]
then
  git config --global core.autocrlf true # windows执行
else
  git config --global core.autocrlf input # Mac或linux执行
fi

log "INFO" "导入git_commit_template(UTF-8 无BOM头格式)"
cp .git_commit_template ~/.git_commit_template
git config --global commit.template .git_commit_template

log "INFO" "更新.npmc文件指向npm源的地址"
cp .npmrc $HOME/

log "INFO" "执行npm install"
if command -v npm > /dev/null; then
  log "INFO" "npm exist"
else
  log "WARN" "npm does not exist"
  log "INFO" "now install nodejs"

  if [[ $SYSTEM =~ "MINGW" ]]; then
    log "INFO" "Windows操作系统开始执行Node安装文件"
    log "INFO" "请下载 https://nodejs.org/dist/v10.16.3/node-v10.16.3-x64.msi 放在该目录下"

    read -p "文件下载完毕, 按任意键继续" var
    cmd.exe /c "start node-v10.16.3-x64.msi" # Windows执行
    read -p "安装完毕, 按任意键继续" var
  elif [[ $SYSTEM =~ "Darwin" ]]; then
    log "INFO" "MacOS开始执行Node安装文件"
    log "INFO" "请下载 https://nodejs.org/dist/v10.16.3/node-v10.16.3.pkg 放在该目录下"
    wget https://nodejs.org/dist/v10.16.3/node-v10.16.3.pkg
    read -p "等待文件下载完毕, 按任意键继续" var

    sudo installer -pkg node-v10.16.3.pkg -target / # MacOS执行
    read -p "安装完毕, 按任意键继续" var
  elif [[ $SYSTEM =~ "Linux" ]]; then
    log "INFO" "Linux系统开始执行Node安装文件"
    log "INFO" "请下载 https://nodejs.org/dist/v10.16.3/node-v10.16.3-linux-x64.tar.xz 放在该目录下"
    wget https://nodejs.org/dist/v10.16.3/node-v10.16.3-linux-x64.tar.xz
    read -p "等待文件下载完毕, 按任意键继续" var

    tar -xf node-v10.16.3-linux-x64.tar.xz
    sudo mv node-v10.16.3-linux-x64 /opt/nodejs
    echo "NODEJS_HOME=/opt/nodejs" >> $HOME/.bash_profile
    echo "PATH=\$NODEJS_HOME/bin\${PATH:+:\${PATH}}" >> $HOME/.bashrc
    echo "export PATH"  >> $HOME/.bashrc
    source $HOME/.bashrc
    read -p "安装完毕, 按任意键继续" var
  fi
fi
log "INFO" '开始npm install, 请等待'
npm i -g cnpm --registry=https://registry.npm.taobao.org
cnpm install
log "INFO" '执行结束'

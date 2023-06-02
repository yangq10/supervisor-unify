# Introduction

[toc]

## 1. 项目介绍

**MTD_Composite_Service_1.2**为三合一后端1.2版本同步框架服务

## 2. 项目开发相关

### 2.1 项目主要架构

Python3、Flask、Mongo、MySQL、RabbitMQ、APM

### 2.2 项目代码目录

```shell
.
├── appcommon(项目级别公共代码,appinstance，errorcode，装饰器等)
├── app
│   ├── cli(项目集成命令行)
│   ├── pay(支付相关业务逻辑)
│   ├── remind(提醒相关业务逻辑)
│   └── urls.py(路由)
├── config
│   ├── env.py
│   ├── http_settings.py(http接口配置)
│   ├── local_settings.template(本地开发配置模板)
│   ├── mtd_libs_settings.py(mtd_libs配置)
│   ├── project_settings.py(项目业务配置))
│   └── settings.py(Flask相关配置)
├── docs(文档)
├── etc
│   └── gunicorn.conf
├── cli.py(命令行工具)
├── requirements_dev.txt(开发依赖)
└── requirements.txt(生产依赖)
```

### 2.3 开发

1 项目环境搭建

```shell
# 虚拟环境（这里使用virtualenvwrapper）
mkvirtualenv -p $(which python3.7) MTD_Composite_Service_1.2
workon MTD_Composite_Service_1.2
pip install -r requirements_dev.txt -q --extra-index-url http://192.168.7.172:8080/simple/

# 项目开发使用flask开发模式
export FLASK_ENV=development

# 复制本地开发配置并自行修改，不修改默认使用config/settings的配置
cp config/local_settings.template config/local_settings.py

# 如需修改mtd_libs的配置，只需要修改config/mtd_libs_settings.py即可

# 注意，开发模式记得设置环境变量FLASK_ENV=development

# pre-commit校验代码规范(自由选择，可加可不加)
pre-commit install
pre-commit run --all-files
```

2 项目启动

```shell
# 推荐
flask run
```

```
# 测试服务器控制台启动方式
sudo su

export MTD_CONF_HOME=/home/mtdadmin/mtdconf

export ENV="develop"

cd /home/mtdadmin/www/MTD_Composite_Server_1.2

/home/mtdadmin/venvs/composite_flask/bin/flask run  --host=0.0.0.0 --port=2108 
```


3 推荐调试用IPython

```shell
python cli.py ipython
python cli.py shell
```

4 其他

```shell
python cli.py --help
```

### 2.4 Gunicorn使用

```shell
# 虚拟环境（这里使用virtualenvwrapper）
mkvirtualenv -p $(which python3.7) MTD_Composite_Service_1.2
workon MTD_Composite_Service_1.2
pip install -r requirements.txt -q --extra-index-url http://192.168.7.172:8080/simple/ --trusted-host 192.168.7.172

# 切记修改系统环境变量ENV为生产模式
export FLASK_ENV=production

# gunicorn启动服务,pid/日志等配置需要自己设定
gunicorn -c etc/gunicorn.conf 'app:create_app()' -p ./gunicorn.pid --access-logfile ./gunicorn_access.log --error-logfile ./gunicorn_error.log
```

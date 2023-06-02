import os

# 当前项目路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 项目名称
PROJECT = os.path.split(BASE_DIR)[-1]

# 使FlaskRestful的异常让@app.errorhander捕获
# https://flask.palletsprojects.com/en/1.0.x/config/#PROPAGATE_EXCEPTIONS
PROPAGATE_EXCEPTIONS = True

SERVERS = {
    "13": {
        "server_desc": "admin@10.98.xx.xx,平台开发组测试应用服务器",
        "api": "http://xx:xx@10.98.xx.xx:9001/RPC2",
    }
}

GROUPS = {
    "service": {
        "group_desc": "价格预测系统服务层",
        "program_list": [
            "13.xx",
            "13.xx",
        ]
    },
    "app": {
        "group_desc": "价格预测系统应用层",
        "program_list": [
            "13.xx",
            "13.xx",
        ]
    },
    "custom": {
        "group_desc": "IDSS外部项目",
        "program_list": [
            "13.xx"
        ]
    }
}
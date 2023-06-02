# -*- coding: UTF-8 –*-
import traceback

from flask import jsonify, request, redirect
from werkzeug.exceptions import NotFound, MethodNotAllowed
from urllib.parse import urlencode
from config import settings


def init(app):
    # @app.before_first_request
    # def before_first():
    #     print("app.before_first")
    #
    # # 钩子函数 before_request
    # @app.before_request
    # def before():
    #     print("app.before")
    #
    # # 钩子函数 after_request
    @app.after_request
    def after(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = '*'
        return response
    #
    # # 钩子函数 teardown_request
    # @app.teardown_request
    # def teardown(e):
    #     print(e)

    @app.errorhandler(Exception)
    def errorhandler(e):
        # if isinstance(e, NotFound) or isinstance(e, MethodNotAllowed):
        #     # 404和405异常不记录到mongo, 统一重定向到首页
        #     return redirect('/')
        if request.method == 'GET':
            query_parameters = urlencode(dict(request.args))
        else:
            query_parameters = urlencode(dict(request.form))

        traceback.print_exc()
        res = {"code": 1003, "msg": "服务器开小差了"}
        return jsonify(res)

from flask import Flask,Blueprint
from dataclasses import dataclass

from injector import inject

from internal.handler import AppHandler

@inject
@dataclass
class Router:

    app_handler: AppHandler

    # def __init__(self, app_handler: AppHandler):
    #     self.app_handler = app_handler

    def register_router(self,app: Flask):
        """注册路由"""
        #1、创建一个蓝图
        bp = Blueprint('llmops',__name__,url_prefix="")

        #2、将url和函数映射到蓝图上
        bp.add_url_rule('/ping', view_func=self.app_handler.ping, methods=['GET'])

        #3、注册蓝图
        app.register_blueprint(bp)


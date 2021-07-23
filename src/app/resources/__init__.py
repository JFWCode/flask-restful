from flask import Blueprint
from flask_restful import Api
from .views import Bugs, Bug

# 定义蓝图，main为蓝图名字
main = Blueprint('main', __name__)
# 实例化api
api = Api(main)

# 设置路由
api.add_resource(Bugs, '/api/v0.1/bugs')
api.add_resource(Bug, '/api/v0.1/bugs/<int:id>')


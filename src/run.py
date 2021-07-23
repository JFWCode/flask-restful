from src.app.resources import main
from flask import Flask
from src.config import Config
from src.app import db


def create_app():
    # 初始化flask
    app = Flask(__name__)
    # 从对象设置配置信息
    app.config.from_object(Config)
    # 第三方扩展初始化
    db.init_app(app)
    # 注册蓝图
    app.register_blueprint(main)
    return app


app = create_app()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

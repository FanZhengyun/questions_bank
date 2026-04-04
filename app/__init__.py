from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__, instance_path=None, instance_relative_config=True)
    app.config.from_object(config_class)

    db.init_app(app)

    # 确保 instance 文件夹存在
    import os
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # 导入模型并创建数据库表
    from app.models import Question
    with app.app_context():
        db.create_all()

    # 注册蓝图路由
    from app.routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app
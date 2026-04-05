from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    env = os.environ.get('FLASK_ENV', 'development')
    app = Flask(__name__, instance_relative_config=True)
    
    if env == 'production':
        # 使用生产配置的工厂方法获取配置字典
        from config import ProductionConfig
        app.config.update(ProductionConfig.get_config())
    else:
        from config import config
        app.config.from_object(config[env])

    # 初始化数据库
    db.init_app(app)

    # 确保 instance 文件夹存在
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
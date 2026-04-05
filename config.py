import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-default-key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'instance', 'questions.db')

class ProductionConfig(Config):
    DEBUG = False
    
    @classmethod
    def get_config(cls):
        """返回生产配置字典，动态检查环境变量"""
        db_uri = os.environ.get('DATABASE_URL')
        if not db_uri:
            raise ValueError("Production environment requires DATABASE_URL to be set")
        secret_key = os.environ.get('SECRET_KEY')
        if not secret_key or secret_key == 'dev-default-key':
            raise ValueError("Production environment requires a strong SECRET_KEY")
        
        return {
            'DEBUG': False,
            'SECRET_KEY': secret_key,
            'SQLALCHEMY_DATABASE_URI': db_uri,
            'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        }

# 配置字典
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,   # 这里存的是类，稍后在 create_app 中特殊处理
    'default': DevelopmentConfig
}
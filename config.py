# 导入操作系统相关的模块，用于处理文件路径
import os


# 基础配置类，包含所有环境通用的配置
class Config:
    # Flask应用的密钥，用于加密会话数据等安全操作
    SECRET_KEY = 'sadasda'

    # SQLAlchemy配置：是否追踪对象的修改（会消耗额外内存）
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 文件上传路径：使用绝对路径，基于当前文件所在目录构建路径
    UP_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "app/static/uploads/")

    # 用户头像上传路径：同样使用绝对路径
    FC_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "app/static/uploads/users/")

    # 静态方法，用于初始化应用时可以添加额外配置
    @staticmethod
    def init_app(app):
        pass


# 开发环境配置类，继承自基础Config类
class DevelopmentConfig(Config):
    # 数据库连接URI，格式为：dialect+driver://username:password@host:port/database
    # 这里使用MySQL数据库，pymysql驱动，连接到本地的travel数据库
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/travel'

    # 开启调试模式，开发时建议开启，生产环境必须关闭
    DEBUG = True


# 配置字典，方便通过名称获取对应的配置类
config = {
    # 默认使用开发环境配置
    'default': DevelopmentConfig
}


# 导入必要的模块和组件
from app import create_app, db  # 从app包导入应用工厂函数和数据库实例
from app.models import *  # 导入所有数据模型（实际项目中建议显式导入）
from flask_script import Manager, Shell  # Flask-Script用于命令行操作
from flask_migrate import Migrate, MigrateCommand  # 数据库迁移支持
from flask import render_template  # 模板渲染

# 创建Flask应用实例
# 'default'参数指定使用的配置（通常对应config.py中的配置类）
app = create_app('default')

# 初始化命令行管理器
manager = Manager(app)


# 初始化数据库迁移工具
# 参数说明：
# - app: Flask应用实例
# - db: SQLAlchemy数据库实例
migrate = Migrate(app, db)

def make_shell_context():
    """
    创建Shell上下文处理器
    返回的字典中的对象会自动注入到flask shell环境中
    """
    return dict(app=app, db=db)

# 添加自定义命令到管理器
manager.add_command("shell", Shell(make_context=make_shell_context))  # 增强版shell
manager.add_command('db', MigrateCommand)  # 数据库迁移命令集

@app.errorhandler(404)
def page_not_found(error):
    """
    自定义404错误处理器
    参数:
        error: 错误对象
    返回:
        渲染的404模板页面和HTTP状态码404
    """
    return render_template("home/404.html"), 404

# 主程序入口,管理员账户admin,密码123456
if __name__ == '__main__':
    # 启动命令行管理器
    # 支持的命令示例:
    # - python manage.py runserver  # 启动开发服务器
    # - python manage.py shell  # 启动交互式shell
    # - python manage.py db init/migrate/upgrade  # 数据库迁移操作
    manager.run()
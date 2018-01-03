# Import flask and template operators
from flask import Flask, render_template, url_for

from flask_bootstrap import Bootstrap
from flask_wtf import CSRFProtect, Form
from .config import config
from flask_admin.base import Admin, MenuLink
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.contrib.sqla import ModelView
bootstrap = Bootstrap()
csrf_token = CSRFProtect()
admin = Admin(template_mode='bootstrap3', name='', url='/')


class MyFileAdmin(FileAdmin):
    form_base_class = Form
    can_upload = False
    can_mkdir = False
    can_rename = True


def create_app():
    app = Flask(__name__)

    app.config.from_object(config)
    bootstrap.init_app(app)
    csrf_token.init_app(app)
    admin.init_app(app)

    from .views import views as views_blueprint
    app.register_blueprint(views_blueprint)

    admin.add_view(MyFileAdmin(config.UPLOAD_FOLDER, name='Downloads'))

    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'), 404

    return app

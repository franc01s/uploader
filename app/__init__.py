# Import flask and template operators
from flask import Flask, render_template, url_for

from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect


from .config import config

bootstrap = Bootstrap()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)

    app.config.from_object(config)
    bootstrap.init_app(app)
    csrf.init_app(app)


    from .views import views as views_blueprint
    app.register_blueprint(views_blueprint)


    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'), 404

    return app
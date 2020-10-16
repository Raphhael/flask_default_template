from flask import Flask
from os import makedirs
from flask_security import Security, current_user

from app.models import db, user_datastore, init_commands
from app.blueprints import public, admin

from app.forms.auth import ExtendedRegisterForm, ExtendedLoginForm


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    try:
        makedirs(app.instance_path)
    except OSError:
        pass

    app.config.from_object('app.config.DevelopmentConfig')
    app.config.from_pyfile(app.config['CFG_FILE'])

    db.init_app(app)
    init_commands(app)

    Security(app, user_datastore, register_form=ExtendedRegisterForm, login_form=ExtendedLoginForm)

    @app.context_processor
    def security_context_processor():
        return dict(current_user=current_user)

    app.register_blueprint(public.bp)
    app.register_blueprint(admin.bp)

    return app

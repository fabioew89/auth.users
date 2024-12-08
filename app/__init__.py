from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from app.controllers.auth import auth_bp
    from app.controllers.users import user_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)

    with app.app_context():
        db.create_all()

    return app

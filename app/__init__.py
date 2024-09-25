from flask import Flask
from app.first.routes import first_bp
from app.second.routes import second_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(first_bp)
    app.register_blueprint(second_bp)

    return app

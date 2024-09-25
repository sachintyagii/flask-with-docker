from flask import Blueprint

second_bp = Blueprint("second", __name__, url_prefix="/second")

@second_bp.route("/home")
def home():
    return "<p>second app</p>"

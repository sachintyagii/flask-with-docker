from flask import Blueprint

first_bp = Blueprint("first", __name__, url_prefix="/first")

@first_bp.route("/home")
def home():
    return "<p>first app</p>"

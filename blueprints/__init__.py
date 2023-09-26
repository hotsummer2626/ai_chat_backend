from flask import Blueprint
from .user import user_bp
from .openai import openai_bp

api = Blueprint('api', __name__, url_prefix='/api')

api.register_blueprint(user_bp)
api.register_blueprint(openai_bp)

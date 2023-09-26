from flask import Blueprint, request, jsonify
from exts import db, ma
from models import User
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token


user_bp = Blueprint('users', __name__, url_prefix='/users')


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_bp.route('/register', methods=['POST'])
def register():
    try:
        email = request.json['email']
        password = request.json['password']

        user = User(email=email, password=generate_password_hash(
            password, method='pbkdf2', salt_length=16))

        db.session.add(user)
        db.session.commit()
        return user_schema.jsonify(user)
    except IntegrityError:
        return jsonify({'error': "User already exists"}), 409
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@user_bp.route('/login', methods=['POST'])
def login():
    try:
        email = request.json['email']
        password = request.json['password']

        user = User.query.filter_by(email=email).first()

        if not user:
            return jsonify({'error': "User not found"}), 404

        if check_password_hash(user.password, password):
            token = create_access_token(identity=user.email)
            return jsonify({'id': user.id, 'email': user.email, 'token': token}), 200
        else:
            return jsonify({'error': "email or password is incorrect"}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500

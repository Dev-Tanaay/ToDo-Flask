from app.extensions import db
from app.models.users import User
from app.utils.validators import validate_signup_data,validate_login_data
from app.utils.tokens import create_token
from flask import jsonify
from werkzeug.security import generate_password_hash , check_password_hash

def signup_user(data):
    error = validate_signup_data(data)
    if error:
        return jsonify({"error": error}), 400

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already exists"}), 400

    new_user = User(
        user_name=name,
        email=email,
        password=generate_password_hash(password) 
    )

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully", "id": new_user.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to create user", "details": str(e)}), 500


def login_user(data):
    error_validation = validate_login_data(data)

    if error_validation:
        return jsonify({"error": error_validation}), 400

    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"error":"User not found"}) , 404

    if not check_password_hash(user.password,password):
        return jsonify({"error":"Invalid credentials"}) , 401

    token = create_token(user)

    return jsonify({"message":"User logged in successfully","user":user.to_dict(),"token":token}),200

     
from functools import wraps
from flask import request , jsonify ,current_app , g
from app.models.users import User
import jwt

def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = None
        if "Authorization" in request.headers:
            auth_header = request.headers["Authorization"]
            try:
                token = auth_header.split(" ")[1]
            except IndexError:
                return jsonify({"error":"Invalid token format"}),401
        
        if not token:
            return jsonify({"error":"Token is missing. Please login"}),401

        try:
            data = jwt.decode(token,current_app.config["SECRET_KEY"],algorithms=["HS256"])
            current_user = User.query.get(data["id"])
            if not current_user:
                return jsonify({"error":"User not found"}),404
            g.user = current_user
        except jwt.ExpiredSignatureError:
            return jsonify({"error":"Token has expired"}),401
        except jwt.InvalidTokenError:
            return jsonify({"error":"Invalid token"}),401

        return f(*args,**kwargs)

    return decorated
            

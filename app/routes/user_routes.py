from flask import Blueprint , request
from app.services import signup_user,login_user
user = Blueprint("user",__name__)

from flask import jsonify

@user.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    response = signup_user(data)
    return response

@user.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    response = login_user(data)
    return response



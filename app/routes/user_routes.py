from flask import Blueprint
from app.services import list_users
user = Blueprint("user",__name__)

@user.route("/user")
def get_user():
    return list_users()


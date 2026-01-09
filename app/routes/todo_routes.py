from flask import Blueprint, request, g
from app.utils.decorators import token_required
from app.services import (
    create_todo_service,
    get_all_todos_service,
    get_todo_service,
    toggle_todo_status_service,
    delete_todo_service,
    update_todo_content_service
)

todo = Blueprint("todo", __name__)

@todo.route("/create", methods=["POST"])
@token_required
def create_todo():
    return create_todo_service(request.get_json(), g.user.id)

@todo.route("", methods=["GET"])
@token_required
def get_all_todos():
    return get_all_todos_service(g.user.id)

@todo.route("/<int:todo_id>", methods=["GET"])
@token_required
def get_todo(todo_id):
    return get_todo_service(todo_id)

@todo.route("/<int:todo_id>", methods=["PUT"])
@token_required
def toggle_todo_status(todo_id):
    return toggle_todo_status_service(todo_id)

@todo.route("/<int:todo_id>", methods=["DELETE"])
@token_required
def delete_todo(todo_id):
    return delete_todo_service(todo_id)

@todo.route("/update/<int:todo_id>", methods=["POST"])
@token_required
def update_todo_content(todo_id):
    return update_todo_content_service(todo_id, request.get_json())

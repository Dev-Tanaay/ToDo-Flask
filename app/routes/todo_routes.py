from flask import Blueprint,request,jsonify,g

todo = Blueprint("todo", __name__)

from app.extensions import db
from app.models.todo import Todo
from app.utils.decorators import token_required

@todo.route("/create", methods=["POST"])
@token_required
def create_todo():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid or missing JSON body"}), 400
    title = data.get("title")
    description = data.get("description")

    if not all([title, description]):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        new_todo = Todo(
            title=title,
            description=description,
            user_id=g.user.id
        )
        db.session.add(new_todo)
        db.session.commit()
        return jsonify({"message": "Todo created successfully", "todo": new_todo.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@todo.route("")
@token_required
def get_all_todos():
    todos = Todo.query.filter_by(user_id=g.user.id).all()
    return jsonify({"todos": [todo.to_dict() for todo in todos]}), 200

@todo.route("/<int:todo_id>", methods=["GET"])
@token_required
def get_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    return jsonify({"todo": todo.to_dict()}), 200

@todo.route("/<int:todo_id>", methods=["PUT"])
@token_required
def toggle_todo_status(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    todo.completed = not todo.completed
    db.session.commit()
    return jsonify({"message": "Todo updated successfully", "todo": todo.to_dict()}), 200

@todo.route("/<int:todo_id>", methods=["DELETE"])
@token_required
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"message": "Todo deleted successfully"}), 200

@todo.route("/update/<int:todo_id>",methods=["POST"])
@token_required
def update_todo_content(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid or missing JSON body"}), 400
    title = data.get("title")
    description = data.get("description" , todo.description)
    todo.title = title
    todo.description = description
    db.session.commit()
    return jsonify({"message": "Todo updated successfully", "todo": todo.to_dict()}), 200
    





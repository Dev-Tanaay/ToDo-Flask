from app.extensions import db
from app.models.todo import Todo
from flask import jsonify

def create_todo_service(data, user_id):
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
            user_id=user_id
        )
        db.session.add(new_todo)
        db.session.commit()
        return jsonify({"message": "Todo created successfully", "todo": new_todo.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def get_all_todos_service(user_id):
    todos = Todo.query.filter_by(user_id=user_id).all()
    return jsonify({"todos": [todo.to_dict() for todo in todos]}), 200

def get_todo_service(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    return jsonify({"todo": todo.to_dict()}), 200

def toggle_todo_status_service(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    todo.completed = not todo.completed
    db.session.commit()
    return jsonify({"message": "Todo updated successfully", "todo": todo.to_dict()}), 200

def delete_todo_service(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"message": "Todo deleted successfully"}), 200

def update_todo_content_service(todo_id, data):
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    
    if not data:
        return jsonify({"error": "Invalid or missing JSON body"}), 400

    title = data.get("title", todo.title)
    description = data.get("description", todo.description)

    todo.title = title
    todo.description = description
    db.session.commit()
    return jsonify({"message": "Todo updated successfully", "todo": todo.to_dict()}), 200

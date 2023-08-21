from .forms import TodoForm
from .db_queries import *
from application import db
from application import app
from flask import jsonify, render_template, request, redirect, flash
from datetime import datetime, timedelta
from dateutil import parser
from bson import ObjectId


@app.route("/")
def get_todos():
    todos = get_todos_from_database()

    return render_template("view_todos_list.html", todos=todos)


@app.route("/add_todo", methods=['POST', 'GET'])
def add_todo():
    if request.method == "POST":
        form = TodoForm(request.form)
        todo_name = form.name.data
        todo_description = form.description.data
        completed = form.completed.data
        priority = form.priority.data
        due_date = datetime.combine(form.due_date.data, datetime.min.time())

        db.todos_flask.insert_one({
            "name": todo_name,
            "description": todo_description,
            "completed": completed,
            "priority": priority,
            "due_date": due_date,
            "date_created": datetime.utcnow()
        })
        flash("Todo successfully added", "success")
        return redirect("/")
    else:
        form = TodoForm()
    return render_template("add_todo.html", form=form)


@app.route("/delete_todo/<id>")
def delete_todo(id):
    db.todos_flask.find_one_and_delete({"_id": ObjectId(id)})
    flash("Todo successfully deleted", "success")
    return redirect("/")


@app.route("/update_todo/<id>", methods=['POST', 'GET'])
def update_todo(id):
    if request.method == "POST":
        form = TodoForm(request.form)
        todo_name = form.name.data
        todo_description = form.description.data
        priority = form.priority.data
        due_date = datetime.combine(form.due_date.data, datetime.min.time())
        completed = form.completed.data

        db.todos_flask.find_one_and_update({"_id": ObjectId(id)}, {"$set": {
            "name": todo_name,
            "description": todo_description,
            "completed": completed,
            "priority": priority,
            "due_date": due_date,
            "date_created": datetime.utcnow()
        }})
        flash("Todo successfully updated", "success")
        return redirect("/")
    else:
        form = TodoForm()

        todo = db.todos_flask.find_one_or_404({"_id": ObjectId(id)})
        form.name.data = todo.get("name", None)
        form.description.data = todo.get("description", None)
        form.priority.data = todo.get("priority", None)
        form.due_date.data = todo.get("due_date", None)
        form.completed.data = todo.get("completed", None)

    return render_template("add_todo.html", form=form)


@app.route('/calendar')
def calendar():
    todos = get_todos_from_database()  # Implement this function to fetch tasks
    return render_template('view_todos_calendar.html', todos=todos)


@app.route('/update_task_due_date', methods=['POST'])
def update_task_due_date():
    data = request.get_json()
    task_id = data.get('task_id')
    new_due_date_str = data.get('new_due_date')
    new_due_date = parser.isoparse(new_due_date_str).date()
    # Convert the datetime.date to datetime.datetime
    new_due_date_datetime = datetime.combine(new_due_date, datetime.min.time()) + timedelta(days=1)

    db.todos_flask.find_one_and_update({"_id": ObjectId(task_id)}, {"$set": {
        "due_date": new_due_date_datetime,
    }})

    return jsonify({"message": "Task due date updated successfully"})

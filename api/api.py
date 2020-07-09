from flask import Flask, jsonify, request
from tasks import tasks
from function_utils import FunctionUtils

app = Flask(__name__)
TASK_NOT_FOUND_MSG = 'Task not found'


# Get all tasks
@app.route('/tasks')
def get_tasks():
    return jsonify(tasks)


# Retrieve a specific task
@app.route('/tasks/<int:task_id>')
def get_task(task_id):
    task_found = FunctionUtils.find_task(task_id)
    if len(task_found) > 0:
        return task_found[0]
    return jsonify({'msg': TASK_NOT_FOUND_MSG})


# Create a task
@app.route('/tasks/', methods=['POST'])
def create_task():
    new_task = {
        "id": request.json['id'],
        "name": request.json['name']
    }
    tasks.append(new_task)
    return jsonify({'msg': 'Task added', 'tasks': tasks})


# Update a task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def edit_task(task_id):
    task_found = FunctionUtils.find_task(task_id)
    if len(task_found) > 0:
        task_found[0]['id'] = request.json['id']
        task_found[0]['name'] = request.json['name']
        return jsonify({'msg': 'Task updated', 'tasks': tasks})
    return jsonify({'msg': TASK_NOT_FOUND_MSG})


# Delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def remove_task(task_id):
    task_found = FunctionUtils.find_task(task_id)
    if len(task_found) > 0:
        tasks.remove(task_found[0])
        return jsonify({'msg': 'Task removed', 'tasks': tasks})
    return jsonify({'msg': TASK_NOT_FOUND_MSG})


# Run the server
if __name__ == '__main__':
    app.run(debug=True, port=4000)
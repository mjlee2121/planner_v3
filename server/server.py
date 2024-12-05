from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# In-memory task list (for simplicity)
tasks = [
    {"id": 1, "title": "Learn React", "description": "Study React basics", "completed": False},
    {"id": 2, "title": "Learn Flask", "description": "Study Flask basics", "completed": False}
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task = {
        "id": len(tasks) + 1,  # Auto-incrementing ID
        "title": data['title'],
        "description": data['description'],
        "completed": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()
    task = next((task for task in tasks if task['id'] == id), None)
    if task:
        task['title'] = data['title']
        task['description'] = data['description']
        task['completed'] = data['completed']
        return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = next((task for task in tasks if task['id'] == id), None)
    if task:
        tasks.remove(task)
        return jsonify({"message": "Task deleted"}), 200
    return jsonify({"error": "Task not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

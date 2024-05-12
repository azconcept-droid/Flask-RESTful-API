#!myvenv/bin/python3
"""Web server module"""

from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks"""

    return jsonify({'tasks': tasks})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Get a single task"""

    task = [task for task in tasks if task['id'] == task_id]

    if len(task) == 0:
        abort(404)

    return jsonify({'task': task[0]})


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    """ Create a new task """

    if not request.json or not 'title' in request.json:
        abort(400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)

    return jsonify({'task': task}), 201


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """ Modify/update task """

    task = [task for task in tasks if task['id'] == task_id]

    if len(task) == 0:
        abort(404)

    if not request.json:
        abort(400)

    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)

    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)

    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)

    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])

    return jsonify({'task': task[0]})

@app.errorhandler(404)
def not_found(error):
    """ Handle 404 error, not found"""

    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, abort, request


app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'name': 'blablabla',
        'check': False

    },
    {
        'id': 2,
        'name': 'blablabla',
        'check': True
    }
]

@app.route('/')
def hello_world():
    return 'Bienvenido! API To-Do List'

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/api/tasks/<int:id>', methods=['GET'])
def get_task(id):
    this_task = [task for task in tasks if task['id'] == id]
    #this_task = 0
    #for task in tasks:
        #if id == task['id']:
            #this_task = task
    if len(this_task) == 0:
        abort(404)
    return jsonify({'task':this_task})

@app.route('/api/tasks', methods = ['POST'])
def create_task():
    if not request.json:
        abort(404)
    task = {
        'id': len(tasks)+1,
        'name': request.json['name'],
        'check': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/api/tasks/<int:task_id>', methods = ['PUT'])
def update_task(task_id):
    this_task = [task for task in tasks if task['id'] == task_id]
    if len(this_task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) is not str:
        abort(400)
    if 'check' in request.json and type(request.json['check']) is not bool:
        abort(400)
    this_task[0]['name'] = request.json.get('name', this_task[0]['name'])
    this_task[0]['check'] = request.json.get('check', this_task[0]['check'])
    return jsonify({'task': this_task[0]})

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task =[task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)


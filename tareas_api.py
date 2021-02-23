from flask import Flask, jsonify, abort, request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

app = Flask(__name__)

cred = credentials.Certificate("firebase_adminsdk.json")
default_app = firebase_admin.initialize_app(cred,{
    'databaseURL':'https://test-api-374a2-default-rtdb.firebaseio.com/'
})

ref = db.reference('/')

@app.route('/')
def hello_world():
    return 'Bienvenido! API To-Do List'

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return ref.get()

@app.route('/api/tasks/<int:id>', methods=['GET'])
def get_task(id):
    if(ref.child("tasks").child(str(id)).get()==None):
        abort(404)
    return jsonify(ref.child("tasks").child(cid).get())

@app.route('/api/tasks', methods = ['POST'])
def create_task():
    if not request.json:
        abort(404)
    id = len(ref.child("tasks").get())
    ref.child("tasks").child(str(id)).set({
        "check": False,
        "name": request.json['name']
    })
    return jsonify(ref.child("tasks").child(str(id)).get()), 201

@app.route('/api/tasks/<int:task_id>', methods = ['PUT'])
def update_task(task_id):
    if ref.child("tasks").child(str(task_id)).get()==None:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) is not str:
        abort(400)
    if 'check' in request.json and type(request.json['check']) is not bool:
        abort(400)
    ref.child("tasks").child(str(id)).update({
        "check": request.json.get('check', ref.child("tasks").child(str(id)).child("check").get),
        "name": request.json.get('name', ref.child("tasks").child(str(id)).child("name").get)
    })
    return jsonify(ref.child("tasks").child(str(task_id)).get())

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task =[task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)


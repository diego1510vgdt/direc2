import os
from flask import Flask, request, jsonify, abort
from firebase_admin import credentials, db, initialize_app

#Inicializar la app con Flask

app = Flask(__name__)

cred = credentials.Certificate('firebase_adminsdk.json')
default_app = initialize_app(cred,{
    'databaseURL':'https://test-api-374a2-default-rtdb.firebaseio.com/'
})

ref = db.reference('tasks')

"""
@app.route('/', methods=['POST'])
def setting():
    ref.set({
        'tasks': {
            '1':{
                'id':'1',
                'name':'Primer tarea',
                'check':False
            }
        }
    })
"""

@app.route('/read', methods=['GET'])
def read():
    try:
        id = request.args.get('id')
        if id:
            return jsonify(ref.child(id).get()), 200
        else: 
            return jsonify(ref.get()), 200
    except Exception as e:
        return f"Ocurrio el siguiente error: {e}"

@app.route('/add', methods=['POST'])
def create():
    try:
        if not request.json:
            abort(404)
        id = str(len(ref.get()))
        task = {
            'id': id,
            'name': request.json['name'],
            'check': False
        }
        ref.child(id).set(task)
        return jsonify({"succes": True}), 200
    except Exception as e:
        return f"Ocurrio el siguiente error: {e}"


@app.route('/update', methods=['PUT'])
def update():
    try:
        id = request.json['id']
        if ref.child(id).get()==None:
            abort(404)
        if not request.json:
            abort(400)
        ref.child(id).update(request.json)
        return jsonify({"succes": True}), 200
    except Exception as e:
        return f"Ocurrio el siguiente error: {e}"

@app.route('/delete', methods=['DELETE'])
def delete():
    try:
        id = request.args.get('id')
        if ref.child(id).get()==None:
            abort(404)
        ref.child(id).delete()
        return jsonify({"succes": True}), 200
    except Exception as e:
        return f"Ocurrio el siguiente error: {e}"

port = int(os.environ.get('PORT',8000))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)
    app.run(debug=True)

#set FLASK_APP=app.py
#flask run
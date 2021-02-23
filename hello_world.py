from flask import Flask, jsonify
import requests


app = Flask(__name__)

alumnos = [
    {
        'id': 1,
        'nombre': 'Maria Fernanda',
        'ap_p': 'Breton',
        'ap_p': 'Quintero',
        'asistencia': 'True'
    },
    {
        'id': 2,
        'nombre': 'Diego',
        'ap_p': 'Vega',
        'ap_p': 'De Ita',
        'asistencia': 'True'
    },
    {
        'id': 2,
        'nombre': 'Luis Alejandro',
        'ap_p': 'Pinot',
        'ap_p': 'Campos',
        'asistencia': 'True'
    }
]

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/alumnos', methods=['GET'])
def get_al():
    return jsonify({'alumnos':alumnos})

#API inception
@app.route('/pkmntype', methods=['GET'])
def get_pkmn():
    ls = 'https://pokeapi.co/api/v2/type'
    response = requests.get(ls)
    json_response = response.json()
    return json_response
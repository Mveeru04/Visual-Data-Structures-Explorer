from flask import Flask, request, jsonify, send_from_directory
from backend import stack, queue, linked_list, binary_tree
import os

app = Flask(__name__, static_folder='frontend')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(app.static_folder, path)

structure_map = {
    'stack': stack,
    'queue': queue,
    'linkedlist': linked_list,
    'binarytree': binary_tree
}

@app.route('/insert/<structure>', methods=['POST'])
def insert(structure):
    data = request.get_json()
    value = data.get('value')
    if structure in structure_map:
        structure_map[structure].insert(value)
        return jsonify(structure_map[structure].get())
    return jsonify([])

@app.route('/remove/<structure>', methods=['POST'])
def remove(structure):
    if structure in structure_map:
        structure_map[structure].remove()
        return jsonify(structure_map[structure].get())
    return jsonify([])

@app.route('/get/<structure>', methods=['GET'])
def get_structure(structure):
    if structure in structure_map:
        return jsonify(structure_map[structure].get())
    return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)

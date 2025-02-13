from flask import Flask, jsonify, request

app = Flask(__name__)

db = {
    'users': [
        {'id': 1, 'name': 'Alice', 'age': 25},
        {'id': 2, 'name': 'Bob', 'age': 30}
    ]
}

@app.route('/get', methods=['GET'])
def get_all():
    return jsonify(db['users'])

@app.route('/get/<int:id>')
def get_id(id):

    if not id:
        return jsonify({'Error':'Necessita de um id'})

    result = next((user for user in db['users'] if user['id'] == id), None)

    if not result:
        return jsonify({'Erro':'Id não existente'})
    else:
        return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
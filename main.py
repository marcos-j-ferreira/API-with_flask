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


@app.route('/post', methods=['POST'])
def post():
    result = request.get_json()
    
    if not result or 'name' not in result or 'age' not in result:
        return jsonify({"error": "Invalid data"}), 400

    name = result['name']
    age = result['age']
    
    if any(user['name'] == name for user in db['users']):
        return jsonify({'error': 'Name already exists'}), 400
    
    new_id = len(db['users']) + 1
    
    db['users'].append({
        'id': new_id, 
        'name': name, 
        'age': age
    })

    return jsonify(db['users']), 201


if __name__ == '__main__':
    app.run(debug=True)
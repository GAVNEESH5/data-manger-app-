from flask import Flask, jsonify, request

app = Flask(_name_)

# In-memory dictionary to store user data
users = {}

# Home route
@app.route('/')
def home():
    return "Welcome to the User Management API!"

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# GET a single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404

# POST (Create a new user)
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user_id = data.get('id')
    if user_id in users:
        return jsonify({'error': 'User already exists'}), 400
    users[user_id] = {'name': data.get('name'), 'email': data.get('email')}
    return jsonify({'message': 'User created'}), 201

# PUT (Update an existing user)
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    if user_id in users:
        users[user_id].update({'name': data.get('name'), 'email': data.get('email')})
        return jsonify({'message': 'User updated'}), 200
    return jsonify({'error': 'User not found'}), 404

# DELETE a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({'message': 'User deleted'}), 200
    return jsonify({'error': 'User not found'}), 404

# Run the app
if _name_ == '_main_':
    app.run(debug=True)
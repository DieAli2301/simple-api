from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de datos simple en memoria
users = []

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    
    if not username or not email:
        return jsonify({'error': 'Username and email are required!'}), 400
    
    user = {'username': username, 'email': email}
    users.append(user)
    
    return jsonify({'message': 'User registered successfully!', 'user': user}), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'users': users}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

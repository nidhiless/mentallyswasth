from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import random

# Initialize Flask and Flask-SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

# List of sample usernames
usernames = ['User1', 'User2', 'User3', 'User4', 'User5']

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the chat page, passing the username to the template
@app.route('/chat')
def chat():
    username = request.args.get('username', f'User{random.randint(1, 1000)}')  # Default to a random user if no username is provided
    return render_template('chat.html', username=username)

# Route for the mood board
@app.route('/mood')
def mood():
    return render_template('mood.html')

# Route for the level page
@app.route('/level')
def level():
    return render_template('level.html')

# Route for the rating page
@app.route('/rating')
def rating():
    return render_template('rating.html')

# Event handler for sending and receiving messages
@socketio.on('send_message')
def handle_message(data):
    # Log the received message from the client for debugging
    print(f"Message from {data['username']}: {data['message']}")
    # Broadcast the message to all connected clients
    socketio.emit('receive_message', data)

# Run the Flask-SocketIO app
if __name__ == '__main__':
    socketio.run(app, debug=True)

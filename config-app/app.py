import os
from flask import Flask

app = Flask(__name__)

# Read the environment variable, default to 'Guest' if it's missing
USER_NAME = os.environ.get('USER_NAME', 'Guest')
PORT = int(os.environ.get('PORT', 5000))

@app.route('/')
def hello():
    return f"Hello, {USER_NAME}! Your app is running on port {PORT}."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
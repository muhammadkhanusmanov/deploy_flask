from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/home')
def home():
    return '<h1> Page <h1>'

# This will run the app on http://localhost:5000
if __name__ == '__main__':
    # Run the app in local network
    app.run(host='0.0.0.0', port=8011)
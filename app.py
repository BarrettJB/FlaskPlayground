from flask import Flask, render_template

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app = Flask(__name__)
    app.run(host = '0.0.0.0', port = 80)
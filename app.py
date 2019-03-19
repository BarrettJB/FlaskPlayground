from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/test')
def test():
    return render_template('playground.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80)
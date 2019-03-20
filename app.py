from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/test')
def test():
    return render_template('playground.html')

@app.route('/html_reference')
def html_reference():
    return render_template('reference.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80)
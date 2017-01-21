from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'

@app.route('/index')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run('127.0.0.1', 20000, True)

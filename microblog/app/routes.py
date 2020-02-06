from app import app
from flask import render_template
@app.route('/')
@app.route('/greet')
def greet():
    return "hello world"

@app.route('/greeting')
def greeting():
    user = {'username': 'Sangamesh K'}
    return render_template('index.html',title='home', user=user)

@app.route('/greet/<name>')
def hello(name):
    return render_template('index.html',title='Home',name=name)

if __name__=='__main__':
    app.run()

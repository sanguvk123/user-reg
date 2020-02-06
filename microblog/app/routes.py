from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm
@app.route('/')
@app.route('/greet')
def greet():
    return "hello world"

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
    
@app.route('/index')
def greeting():
    user = {'username': 'Sangamesh K'}
    return render_template('index.html',title='home', user=user)

@app.route('/greet/<name>')
def hello(name):
    return render_template('index.html',title='Home',name=name)

if __name__=='__main__':
    app.run()

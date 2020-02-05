from app import app

@app.route('/')
@app.route('/greet')
def greet():
    return "hello world"

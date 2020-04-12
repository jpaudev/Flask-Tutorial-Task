from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World! I'm done with Chapter 1!"
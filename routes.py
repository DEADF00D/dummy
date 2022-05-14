from pico import app

@app.route('/')
def index():
    return '<h1>This should work !</h1>'

from app import app

@app.route('/')
def index():
    return 'This is flask'
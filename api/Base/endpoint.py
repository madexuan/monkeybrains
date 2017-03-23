from server import app


@app.route('/')
def get_index():
    version = '1.0.0'
    return version
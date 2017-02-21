from flask import Flask


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')


# import from api package at the end of the file here to
# circumvent circular import issues
# http://flask.pocoo.org/docs/0.11/patterns/packages/#larger-applications
# import api.views

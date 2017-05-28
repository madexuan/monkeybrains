from flask import Flask


app = Flask(__name__)
app.config.from_object('config')


# import from api package at the end of the file here to
# circumvent circular import issues
# http://flask.pocoo.org/docs/0.11/patterns/packages/#larger-applications
# import api.views

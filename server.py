from flask import Flask
import flask_login


app = Flask(__name__)
app.config.from_object('config')
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

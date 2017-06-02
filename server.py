from flask import Flask
import flask_login
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config.from_object('config')
bcrypt = Bcrypt(app)
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

from flask import Flask
import flask_login
from flask_bcrypt import Bcrypt
from flask_mail import Mail


app = Flask(__name__, template_folder='api/templates')
app.config.from_object('config')
bcrypt = Bcrypt(app)
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
mail = Mail(app)

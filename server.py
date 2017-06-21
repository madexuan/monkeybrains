from flask import Flask
import flask_login
from flask_bcrypt import Bcrypt
import sendgrid
import os


app = Flask(__name__, template_folder='api/templates')
app.config.from_object('config')
bcrypt = Bcrypt(app)
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

# initialize sendgrid
sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

import os

# flask
SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', default="fillthisin")
DEBUG = os.environ.get('FLASK_DEBUG', default=False)  # always set debug to false in production

# sqlalchemy
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', default='postgresql://localhost/monkeys')
SQLALCHEMY_TRACK_MODIFICATIONS = False

import os

# flask
SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', default="fillthisin")
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', default='postgresql://localhost/monkeys')
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = os.environ.get('FLASK_DEBUG', default=False)  # always set debug to false in production

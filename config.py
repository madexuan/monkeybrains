import os

# flask
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('FLASK_DEBUG', default=False)  # always set debug to false in production

# sqlalchemy
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', default='postgresql://localhost/monkeys')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# flask_bcrypt
BCRYPT_LOG_ROUNDS = 12

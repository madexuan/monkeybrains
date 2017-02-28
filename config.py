import os


SECRET_KEY = 'fillthisin'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', default='postgresql://localhost/monkeys')
USERNAME = 'admin'
PASSWORD = 'default'
DEBUG = False  # always set debug to false in production

import os


SECRET_KEY = 'fillthisin'
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
USERNAME = 'admin'
PASSWORD = 'default'
DEBUG = False  # always set debug to false in production

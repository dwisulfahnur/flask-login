""" Base Configuration """

import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__name__))
APP_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

SECRET_KEY = '4ku 4n4k s3h4t'
ASSETS_DEBUG = False
CACHE_TYPE = 'simple'

# SECURITY CONFIG
SECURITY_REGISTERABLE = True
SECURITY_RECOVERABLE = True
SECURITY_CONFIRMABLE = False
SECURITY_TRACKABLE = True
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = 's3h4t 1tu 1nd4h'
CSRF_ENABLED = True
CSRF_SESSION_KEY = 'hdsdf4h'
# DATABASE CONFIG
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(PROJECT_DIR, 'app.db')

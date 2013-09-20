import os

APP_DEBUG = True

CSRF_ENABLED = True
SECRET_KEY = '<MAKE UP A SECRET KEY> '

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql://<YOUR-DATABASE-USERNAME>:<YOUR-EB-DATABASE-PASSWORD>@<YOUR-DATABASE-ENDPOINT>/<YOUR-EB-DATABASE-NAME>'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
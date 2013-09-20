#!flask/bin/python

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# The WSGI configuration on Elastic Beanstalk requires
# the callable be named 'application' by default.
application = Flask(__name__)
application.config.from_object('config')

db = SQLAlchemy(application)

from app import views, models
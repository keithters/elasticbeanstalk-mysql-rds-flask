#!flask/bin/python

from app import application
import config

if __name__ == '__main__':
	application.run(debug=config.APP_DEBUG)
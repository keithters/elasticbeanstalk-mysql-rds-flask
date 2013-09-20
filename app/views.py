from flask import render_template, send_from_directory
from app import application
from models import User


# Setup the root route of the website, and render the 'index.html' template
@application.route("/")
def default():
	return render_template('index.html')


@application.route("/testdb")
def testdb():

	if User.query.first():
		u = User.query.first()
		return render_template('testdb.html', title='Success!', nickname=u.nickname)
	else:
		return render_template('testdb.html', title='Fail!')


@application.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(application.root_path, 'static'), 'favicon.ico',
	                           mimetype='image/vnd.microsoft.icon')

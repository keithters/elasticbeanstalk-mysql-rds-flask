elasticbeanstalk-mysql-rds-flask
================================

A Simple Flask (python) base application using Amazon Elastic Beanstalk with an Amazon MySQL RDS.  
Follow the instructions below to get up and running.

####From Terminal:
    $ git clone <this repo>
    $ cd elasticbeanstalk-mysql-rds-flask
    $ python virtualenv.py flask
    $ flask/bin/pip install -r requirements.txt


####Then:
Download and install the command line tools http://aws.amazon.com/code/6752709412171743


####Back in Terminal set up eb tools and create an eb app:
If you need to find your security creds, look here: http://docs.aws.amazon.com/general/latest/gr/getting-aws-sec-creds.html
    
    $ export PATH=$PATH:<path to unzipped EB CLI package>/eb/macosx/python2.7/  
*(if not on macosx, change this path appropriate to your platform)*
    
    $ eb init
    (Answer the questions)
    Enter an AWS Elastic Beanstalk environment name (current value is ""): *(NOTE: this must be <= 23 chars & can't end in a hyphen)*
    Select a solution stack (current value is "32bit Amazon Linux running Python").
    Create RDS instance? [y/n]: y
    Attach an instance profile (current value is "aws-elasticbeanstalk-ec2-role"):
    $ eb start


####In a browser give your machine security clearance:
* Log in to your AWS account and go to https://console.aws.amazon.com/rds/home
* Click "Security Groups" -> "Create DB Secutity Group" *(if you don't see security groups in the left nav, make sure the correct region is selected in the top right)*
* Add the CDIR of your current machine *(if you are behind a firewall you may need to find your external CDIR)*
* Click 'Instances'
* To add your new security group, edit your RDS instance: "Instance Actions" -> "Modify" and select all the necessary groups


####Edit Option settings and config files
Edit __.elasticbeanstalk/optionsettings.YOUR-EB-ENV__ to include this:

    [aws:elasticbeanstalk:container:python:staticfiles]
    /static/=app/static
    /favicon.ico=app/static/favicon.ico

    [aws:elasticbeanstalk:container:python]
    StaticFiles=/static/=app/static/,/favicon.ico=app/static/favicon.ico

Edit __config.py__:

    SECRET_KEY = <MAKE UP A SECRET KEY>  
    SQLALCHEMY_DATABASE_URI = 'mysql://<YOUR-DATABASE-USERNAME>:<YOUR-EB-DATABASE-PASSWORD>@<YOUR-DATABASE-ENDPOINT>/<YOUR-EB-DATABASE-NAME>'


###Make your db:
    $ flask/bin/python db_create.py
    $ flask/bin/python db_migrate.py


####Update and run the thing:
    $ eb update
    $ git commit -am "just in case something needs to be committed"
    $ git aws.push
    $ eb status --verbose


###Make sure everything worked and it's running:
* Go to https://console.aws.amazon.com/console/
* Click on "Elastic Beanstalk" -> YOUR-ENV
* Click the link at the top of the page *(your eb URL)*
* Voila!


###Put a record in the database to make sure it's working:
    $ flask/bin/python

    >>> from app import application, models, db  
    >>> import config  
    >>> u = models.User(nickname='ringo')  
    >>> db.session.add(u)  
    >>> db.session.commit()  

* Go to your-eb-url/testdb and see if it worked. if so, you're in business.



Much gratitude owed (and some code should be credited to) to the Flask Mega Tutorial. (http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

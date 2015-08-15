# Load in Flask, Bootstrap, Our security libs, mail, and a Mongo Driver
from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.mongoengine import MongoEngine
from flask.ext.security import Security, MongoEngineUserDatastore, login_required
from flask_security.core import current_user
from flask_mail import Mail

# pull in our models, and web forms
from models import User, Role
from forms import ExtendedConfirmRegisterForm

# Grab our configuration
from config import secret_key, pwhash, salt, mongo_db, mongo_host, mongo_port, \
            user_enable_registration, user_enable_tracking, user_from_email, user_register_email_subject, \
            mail_url, mail_SSL, mail_port, mail_TLS, mail_user, mail_pass


app = Flask(__name__)

app.config['DEBUG'] = False
app.config['SECRET_KEY'] = secret_key

# MongoDB Config
app.config['MONGODB_DB'] = mongo_db
app.config['MONGODB_HOST'] = mongo_host
app.config['MONGODB_PORT'] = mongo_port

#Security Features
app.config['SECURITY_REGISTERABLE'] = user_enable_registration
app.config['SECURITY_TRACKABLE'] = user_enable_tracking
app.config['SECURITY_EMAIL_SENDER'] = user_from_email
app.config['SECURITY_PASSWORD_HASH'] = pwhash
app.config['SECURITY_PASSWORD_SALT'] = salt
app.config['SECURITY_CONFIRMABLE'] = True
app.config['SECURITY_EMAIL_SUBJECT_REGISTER'] = user_register_email_subject

# Email
app.config['MAIL_SERVER'] = mail_url
app.config['DEBUG'] = False
app.config['MAIL_PORT'] = mail_port
app.config['MAIL_USE_SSL'] = mail_SSL
app.config['MAIL_USE_TLS'] = mail_TLS
app.config['MAIL_USERNAME'] = mail_user
app.config['MAIL_PASSWORD'] = mail_pass 
app.config['MAIL_SUPPRESS_SEND'] = False


# Create database connection object
db = MongoEngine(app)
#Bootstrap
Bootstrap(app)
#Setup Mail
mail = Mail(app)
mail.init_app(app)

    # mail test
with mail.record_messages() as outbox:
    mail.send_message(subject='testing',
                      body='test',
                      recipients=['ryan@solidarray.com'])

    assert len(outbox) == 1
    assert outbox[0].subject == "testing"


# Setup Flask-Security
user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore, confirm_register_form=ExtendedConfirmRegisterForm)
#security = Security(app, user_datastore)


@app.route('/')
def index():
  return render_template('index.html')

if __name__ == "__main__":
  app.run(debug=True,port=5000,host="0.0.0.0")

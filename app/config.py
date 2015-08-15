# You can gen a bcrypt hash here:
##    http://bcrypthashgenerator.apphb.com/

pwhash = 'bcrypt'

# You can generate salts and other secrets with openssl
# For example:
#   $ openssl rand -hex 16
#   1ca632d8567743f94352545abe2e313d
salt = "141202e6b20aa53596a339a0d0b92e79"
secret_key = 'fe65757e00193b8bc2e18444fa51d873'

mongo_db = 'mydatabase'
mongo_host = 'localhost'
mongo_port = 27017

user_enable_registration = True
user_enable_tracking = True
user_from_email = "noreply@yoursite.com"
user_register_email_subject = "Thank you for signing up"

mail_url = "mail.yoursite.com"
mail_port = "25"
mail_SSL = False
mail_TLS = False
mail_user = "username_goes_here"
mail_pass = "password_goes_here"



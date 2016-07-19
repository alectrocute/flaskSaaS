TIMEZONE = 'Europe/Paris'

# Secret key for generating tokens
SECRET_KEY = 'houdini'

# Admin credentials
ADMIN_CREDENTIALS = ('admin', 'pa$$word')

# Database choice
SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Configuration of a Gmail account for sending mails
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'flask.boilerplate'
MAIL_PASSWORD = 'flaskboilerplate123'
ADMINS = ['flask.boilerplate@gmail.com']

# Number of times a password is hashed
BCRYPT_LOG_ROUNDS = 12

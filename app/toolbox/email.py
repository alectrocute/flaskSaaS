from threading import Thread
from flask.ext.mail import Message
from app import app, mail


def send(recipient, subject, body):
    '''
    Send a mail to a recipient. The body is usually a rendered HTML template.
    The sender's credentials has been configured in the config.py file.
    '''
    sender = app.config['ADMINS'][0]
    message = Message(subject, sender=sender, recipients=[recipient])
    message.html = body
    # Create a new thread
    thr = Thread(target=send_async, args=[app, message])
    thr.start()


def send_async(app, message):
    ''' Send the mail asynchronously. '''
    with app.app_context():
        mail.send(message)
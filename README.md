# Flask boilerplate code

![License](http://img.shields.io/:license-mit-blue.svg)

I didn't really like the Flask starter projects I found searching the web. I really like Flask and I use it for quite a few projects so I decided to make a clean, readable, documented starter project. I didn't include any [makefile](https://www.wikiwand.com/en/Makefile) or [fabric](http://flask.pocoo.org/docs/0.10/patterns/fabric/) as I feel it imposes a choice to the user of this project, I rather keep things simple (even though the word is subject to interpretation).

## Features

- [x] User account sign up, sign in, password reset, all through asynchronous email confirmation.
- [x] Form generation.
- [x] Error handling.
- [x] HTML macros and layout file.
- [x] "Functional" file structure.
- [x] Python 3.x compliant.
- [x] Asynchronous AJAX calls.
- [ ] Application factory.
- [x] Administration panel.
- [ ] Static file bundling, automatic SCSS to CSS conversion and automatic minifying.
- [ ] Websockets (for example for live chatting)
- [x] Virtual environment example.
- [ ] Heroku deployment example.
- [x] Digital Ocean deployment example.
- [ ] Tests.
- [ ] Logging.
- [ ] Language selection.
- [ ] Automatic API views.
- [ ] API key generator.

If you have any suggestions or want to help, feel free to drop me a line at <maxhalford25@gmail.com> or to create an issue.

## Libraries

### Backend

- [Flask](http://flask.pocoo.org/), obviously.
- [Flask-Login](https://flask-login.readthedocs.org/en/latest/) for the user accounts.
- [Flask-SQLAlchemy](https://pythonhosted.org/Flask-SQLAlchemy/) interacting with the database.
- [Flask-WTF](https://flask-wtf.readthedocs.org/en/latest/) and [WTForms](https://wtforms.readthedocs.org/en/latest/) for the form handling.
- [Flask-Mail](https://pythonhosted.org/Flask-Mail/) for sending mails.
- [itsdangerous](http://pythonhosted.org/itsdangerous/) for generating random tokens for the confirmation emails.
- [Flask-Bcrypt](https://flask-bcrypt.readthedocs.org/en/latest/) for generating secret user passwords.
- [Flask-Admin](https://flask-admin.readthedocs.org/en/latest/) for building an administration interface.

### Frontend

- [Semantic UI](http://semantic-ui.com/) for the global style. Very similar to [Bootstrap](http://getbootstrap.com/).
- [Leaflet JS](http://leafletjs.com/) for the map. I only added for the sake of the example.

## Structure

I did what most people recommend for the application's structure. Basically, everything is contained in the ``app/`` folder.

- There you have the classic ``static/`` and ``templates/`` folders. The ``templates/`` folder contains macros, error views and a common layout.
- I added a ``views/`` folder to separate the user and the website logic, which could be extended to the the admin views.
- The same goes for the ``forms/`` folder, as the project grows it will be useful to split the WTForms code into separate files.
- The ``models.py`` script contains the SQLAlchemy code, for the while it only contains the logic for a ``users`` table.
- The ``toolbox/`` folder is a personal choice, in it I keep all the other code the application will need.


## Setup

### Vanilla

- Install the required libraries.

	``pip install -r requirements.txt``

- Create the database.

	``python createdb.py``

- Run the application.

	``python run.py``

- Navigate to ``localhost:5000``.


### Virtual environment

```
pip install virtualenv
virtualenv venv
venv/bin/activate (venv\scripts\activate on Windows)
pip install -r requirements.txt
python createdb.py
python run.py
```


## Deployment

- Heroku
- [Digital Ocean](deployment/Digital-Ocean.md)


## Configuration

The goal is to keep most of the application's configuration in a single file called ``config.py``. The one I have included is basic and yet it covers most of the important stuff.

I have included a working Gmail account to confirm user email addresses and reset user passwords, although in production you should't include the file if you push to GitHub because people can see it. The same goes for API keys, you should keep them secret. You can read more about secret configuration files [here](https://exploreflask.com/configuration.html).

Read [this](http://flask.pocoo.org/docs/0.10/config/) for information on the possible configuration options.


## Examples

- [Screenshots](screenshots/)


## Inspiration

- [The Flask Mega-Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).
- [Explore Flask](https://exploreflask.com/index.html).


## Other possibilities

- [flask-boilerplate](https://github.com/mjhea0/flask-boilerplate) by [Michael Herman](https://github.com/mjhea0).
- [Flask-Foundation](https://github.com/JackStouffer/Flask-Foundation) by [Jack Stouffer](https://github.com/JackStouffer).
- [fbone](https://github.com/imwilsonxu/fbone) by [Wilson Xu](https://github.com/imwilsonxu).

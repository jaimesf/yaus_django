# Yet Another Url Shorterner in Django (Python 3.4)

Created with virtualenv, but it works without it too

### Requirements

* Python 3
* Pip 3 (To install dependencies)
* MongoDB
* Django 1.9
* PyMongo 2.8
* Mongoengine 0.9.0

You can install all python dependencies executing _pip3 install -r requirements.txt_

### Configs

* Change connect data for mongodb database on yaus/settings.py

* Change yaus/settings.PROTOCOL to your server protocol

* Change yaus/settings.HOSTNAME to your server hostname

* Change yaus/settings.PORT to your server protocol if necessary (No needed on port 80, or 443 on https)

To run YAUS, execute _python3 manage.py runserver localhost:8000_

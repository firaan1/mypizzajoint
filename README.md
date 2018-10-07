# Project 3: ** *My*Pizzajoint**

Web Programming with Python and JavaScript

## Download
``` bash
git clone https://github.com/firaan1/mypizzajoint.git
```
## Start ** *My*Pizzajoint**
In order to setup the database, import data and start this app for the first time, please follow the instructions below,
``` bash
# Install required python packages from requirements.txt file
pip install -r requirements.txt
# create database tables using django
python manage.py makemigrations
python manage.py migrate
# input data into database
python prep.py
# create admin user with your own username and password to access admin page
python manage.py createsuperuser
# start django server
python manage.py runserver
```

# Project 3: ** *My*Pizzajoint**

Web Programming with Python and JavaScript

This application was developed using Python Django, HTML, Javascript and CSS.
This web page allows the users to register / login and order your favorite pizza, pasta, subs and salads online. The admin of this site can add / delete menu items. The admin can also check the placed orders and change the order status. All orders can be paid by credit card.

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
python manage.py shell < prep.py
# create admin user with your own username and password to access admin page
python manage.py createsuperuser
# start django server
python manage.py runserver
```

## Contents
The directory structure is shown below
``` bash
mypizzajoint/
├── db.sqlite3 # database (will be created by the admin from commandline)
├── manage.py # django file
├── orders # django app
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations # database migration folder (files are removed for convenience)
│   ├── models.py # database models used in this app
│   ├── __pycache__ # files are removed for convenience
│   ├── static # static folder
│   │   └── orders # app folder
│   │       ├── img1.jpg
│   │       ├── mystyle.css
│   │       └── pizza_pattern.jpeg
│   ├── templates # folder containing html files
│   │   └── orders # app folder
│   │       ├── change_order.html # add/delete order html (used internally)
│   │       ├── index.html # home folder
│   │       ├── layout.html # base html file for all other html templates
│   │       ├── login.html # user login html
│   │       ├── make_payment.html # template to handle payment
│   │       ├── order.html # html to place menu order
│   │       ├── register.html # user registration
│   │       └── show_order.html # html for showing selected orders
│   ├── tests.py
│   ├── urls.py # python file containing url definitions
│   └── views.py # python function  definitions
├── pizza
│   ├── __init__.py
│   ├── __pycache__ # files are removed for convenience
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── prep.py # python file containing menu informations to feed to database
├── README.md # readme file
└── requirements.txt # python package requirements
```

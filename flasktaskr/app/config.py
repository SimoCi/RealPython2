# config.py


import os
from keys import THE_KEY

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = THE_KEY

DATABASE_PATH = os.path.join(basedir, DATABASE)
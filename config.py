# config.py
import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/db_amirulpay'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

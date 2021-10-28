import os

class Config(object):
    SECRET_KEY = 'my_secret_key'


class DevelopmentConfig(Config):
    DEBUG =True
    #SQLALCHEMY_DATABAS_URI = 'sqlite:///database\cholula.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
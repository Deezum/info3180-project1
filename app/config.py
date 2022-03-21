import os



class Config(object):
    """Base Config Object"""
    DEBUG = False
    UPLOAD_FOLDER = './uploads'

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('DATABASE_URL') 


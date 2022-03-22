import os



class Config(object):
    """Base Config Object"""
    DEBUG = False
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')

    SECRET_KEY = os.environ.get('SECRET_KEY','Som3$ec5etK*y')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace('postgres://', 'postgresql://')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


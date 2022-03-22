import os



class Config(object):
    """Base Config Object"""
    DEBUG = False
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
    SECRET_KEY = os.environ.get('SECRET_KEY','Som3$ec5etK*y')
    SQLALCHEMY_DATABASE_URI ="postgresql://ukfjaohwpbrruc:2de9caefa25db51307d2816b0feea7ae6c32ff9bca746f6e2e21c9b5b6ec0c93@ec2-34-224-226-38.compute-1.amazonaws.com:5432/d8lu1g95lmjroa"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


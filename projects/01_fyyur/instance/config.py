
import os

# Generate the 32 bit secret key.....
SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@localhost:5432/fyyurdb'
SQLALCHEMY_TRACK_MODIFICATIONS = False
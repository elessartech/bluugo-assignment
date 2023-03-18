import os

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = True

DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 2

ERROR_404_HELP = False

CSRF_ENABLED = True

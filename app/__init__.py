from flask import Flask

app = Flask(__name__)
from app import views

""" creates application object (class Flask) and imports
the views module """

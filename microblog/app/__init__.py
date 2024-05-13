#!myvenv/bin/python3
"""Initializes the Flask app"""

from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes

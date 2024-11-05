#!/usr/bin/env python3
"""1-app Module
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    LANGUAGES = ["en", "fr"]


# Flask app instance
app = Flask(__name__)

# Instantiate the Babel object
babel = Babel(app)

# Set app configuration from the Config class
app.config.from_object(Config)


@app.route("/")
def index():
    """Homepage
    """
    return render_template('1-index.html')

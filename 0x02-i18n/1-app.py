#!/usr/bin/env python3
"""1-app Module
"""
from flask import Flask, render_template
from flask_babel import Babel, _


class Config:
    """Config class for babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "es"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Flask app instance
app = Flask(__name__)

# Set app configuration from the Config class
app.config.from_object(Config)

# Instantiate the Babel object
babel = Babel(app)


@app.route("/")
def index():
    """Homepage
    """
    return render_template('1-index.html')

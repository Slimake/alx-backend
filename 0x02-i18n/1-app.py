#!/usr/bin/env python3
"""1-app Module
"""
from flask import Flask, render_template
from flask_babel import Babel

# Instantiate the Babel object
babel = Babel()


class Config:
    """Config class for babel
    """
    LANGUAGES = ["en", "fr"]
    LANG_DEFAULT = "en"
    TIMEZONE_DEFAULT = "UTC"


# Flask app instance
app = Flask(__name__)

# Set app configuration from the Config class
app.config.from_object(Config)

babel.init_app(app)

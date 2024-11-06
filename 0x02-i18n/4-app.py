#!/usr/bin/env python3
"""4-app Module
"""
from flask import Flask, request, render_template
from flask_babel import Babel
from typing import Any


class Config:
    """Config class for babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Flask app instance
app = Flask(__name__)

# Set app configuration from the Config class
app.config.from_object(Config)


def get_locale() -> Any:
    """Get locale from the user's browser
    """
    query_string_dict = dict(request.args)
    if 'locale' in query_string_dict and \
       query_string_dict['locale'] in Config.LANGUAGES:
        return query_string_dict['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# Instantiate the Babel object
babel = Babel(app, locale_selector=get_locale)


@app.route("/")
def index():
    """Homepage
    """
    return render_template('4-index.html')

#!/usr/bin/env python3
"""6-app Module
"""
from flask import Flask, request, render_template, g
from flask_babel import Babel
from typing import Any, Union


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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

# Instantiate the Babel object
babel = Babel(app)


@babel.localeselector
def get_locale() -> Any:
    """Get locale from the user's browser
    """
    # Check for 'locale' parameter in url
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale

    # Check for 'locale' in user settings (g.user)
    if g.user and g.user['locale'] in Config.LANGUAGES:
        return g.user['locale']

    # Check the Accept-Language header from browser settings
    accept_lang = request.accept_languages.best_match(app.config['LANGUAGES'])
    if accept_lang:
        return accept_lang

    # Default locale
    return Config.BABEL_DEFAULT_LOCALE


def get_user():
    """Return a user dictionary or None if login_as in not provided
    """
    login_id = request.args.get('login_as')
    if login_id is not None:
        login_id = int(login_id)
    if login_id and login_id in users:
        return users.get(login_id)
    return None


@app.before_request
def before_request():
    """Set the user in g.user
    """
    g.user = get_user()


@app.route("/")
def index():
    """Homepage
    """
    return render_template('6-index.html', user=g.user)

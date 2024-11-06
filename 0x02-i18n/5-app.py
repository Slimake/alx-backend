#!/usr/bin/env python3
"""5-app Module
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
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> object:
    login_id: Union[str, int, None] = request.args.get('login_as')
    if login_id is not None:
        login_id = int(login_id)
    if login_id and login_id in users:
        return users.get(login_id)
    return None


@app.before_request
def before_request():
    g.user = get_user()


@app.route("/")
def index():
    """Homepage
    """
    locale = get_locale()
    return render_template('5-index.html', locale=locale, user=g.user)

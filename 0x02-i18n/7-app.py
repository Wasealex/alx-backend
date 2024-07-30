#!/usr/bin/env python3
"""a simple flask app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Optional


class Config:
    """Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)

app.config.from_object(Config)
babel = Babel(app)


def get_user() -> Optional[dict]:
    """GET method to retrieve user information
    """
    login_as = request.args.get('login_as')
    if login_as is None:
        return None
    user = users.get(int(login_as))
    if user is None:
        return None
    return user


@app.before_request
def before_request() -> None:
    """Function executed before all other functions"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """get locale
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        print(locale)
        return locale

    if g.user:
        locale = g.user.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale

    locale = request.headers.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """get timezone
    """
    timezone = request.args.get('timezone')
    if timezone:
        return timezone

    if g.user:
        timezone = g.user.get('timezone')
        if timezone:
            return timezone
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """GET method
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)

#!/usr/bin/env python3
"""a simple flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)

app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale():
    """get locale
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """GET method
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)

#!/bin/python3
"""Controller logic for mini."""

import gestalt
from bottle import (TEMPLATE_PATH, Bottle, debug, error, run, static_file,
                    template)

app = Bottle()

# append to bottle.TEMPLATE_PATH so views are correctly found by pytest
TEMPLATE_PATH.append('mini/views/')

# set debug(True) for testing
debug(True)


@app.route('/')
def index():
    """Return index template."""
    return(template('index'))


@app.route('/favicon.ico', method='GET')
def get_favicon():
    """Return the favicon."""
    return static_file('favicon.ico', root='static/')


@app.route('/mini.css', method='GET')
def get_css():
    """Return the stylesheet."""
    return static_file('mini.css', root='static/')


@error(404)
def missing(code):
    """Return 404 template."""
    return(template('404'))


@error(500)
def error(code):
    """Return 500 template."""
    return(template('500'))


@app.route('/hello/<name>')
def helloname(name):
    """Return hello_name template for testing."""
    return(template('hello_name', name=name))


if __name__ == '__main__':
    settings = gestalt.LoadConfig('config.ini')
    run(app, host=settings.host, port=settings.port, reloader=True)

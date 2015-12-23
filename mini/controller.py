#!/bin/python3
"""Controller logic for mini."""

import requests

import gestalt
from bottle import TEMPLATE_PATH, debug, route, run, static_file, template

# append to bottle.TEMPLATE_PATH so views are correctly found by pytest
TEMPLATE_PATH.append('mini/views/')

# set debug(True) for testing
debug(True)


@route('/')
def index():
    """Return index template."""
    return(template('index'))


@route('/favicon.ico', method='GET')
def get_favicon():
    """Return the favicon."""
    return static_file('favicon.ico', root='static/')


@route('/mini.css', method='GET')
def get_favicon():
    """Return the stylesheet."""
    return static_file('mini.css', root='static/')


@route('/hello/<name>')
def helloname(name):
    """Return hello_name template for testing."""
    return(template('hello_name', name=name))


if __name__ == '__main__':
    settings = gestalt.LoadConfig('config.ini')
    run(host=settings.host, port=settings.port, reloader=True)

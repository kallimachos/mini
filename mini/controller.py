#!/bin/python3
"""Controller logic for mini."""

import requests

import gestalt
from bottle import TEMPLATE_PATH, debug, route, run, template

# append to bottle.TEMPLATE_PATH so views are correctly found by pytest
TEMPLATE_PATH.append('mini/views/')

# set debug(True) for testing
debug(False)


@route('/')
def index():
    """Return index template."""
    return(template('index'))


@route('/hello/<name>')
def helloname(name):
    """Return hello_name template for testing."""
    return(template('hello_name', name=name))


def checkresponse(url):
    """Confirm connection to the server."""
    try:
        r = requests.get(url)
        return(r.status_code)
    except Exception as e:
        print('An error occured:\n' + str(e))
        return(1)


if __name__ == '__main__':
    settings = gestalt.LoadConfig('config.ini')
    run(host=settings.host, port=settings.port, reloader=True)

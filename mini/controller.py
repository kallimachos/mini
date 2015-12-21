#!/bin/python3

import conf
import requests
from bottle import route, run, template, debug, TEMPLATE_PATH

# append to bottle.TEMPLATE_PATH so views are correctly found by pytest
TEMPLATE_PATH.append('mini/views/')

# set debug(True) for testing
debug(False)


@route('/')
def index():
    print(TEMPLATE_PATH)
    return(template('index'))


@route('/hello/<name>')
def helloname(name):
    return(template('hello_name', name=name))


def checkresponse(url):
    try:
        r = requests.get(url)
        return(r.status_code)
    except Exception as e:
        print('An error occured:\n' + str(e))
        return(1)


if __name__ == '__main__':
    settings = conf.LoadConfig('config.ini')
    run(host=settings.host, port=settings.port, reloader=True)

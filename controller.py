#!/bin/python3

import configparser
import requests
from bottle import route, run, template, debug

# set debug(True) for testing
debug(False)


@route('/')
def index():
    return(template('index'))


@route('/test')
def test():
    return('<h1>Test</h1>')


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


def loadConfig():
    config = configparser.ConfigParser()
    config.read('config.ini')
    protocol = config['DEFAULT']['protocol']
    host = config['DEFAULT']['host']
    port = config['DEFAULT']['port']
    indexURL = protocol + '://' + host + ':' + port + '/'
    settings = {'protocol': protocol, 'host': host, 'port': port,
                'indexURL': indexURL}
    return(settings)


if __name__ == '__main__':
    config = loadConfig()
    run(host=config['host'], port=config['port'], reloader=True)

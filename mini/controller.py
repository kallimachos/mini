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
    '''
    >>> test()
    '<h1>Test</h1>'
    >>>
    '''
    return('<h1>Test</h1>')


@route('/hello/<name>')
def helloname(name):
    return(template('hello_name', name=name))


def checkresponse(url):
    '''
    >>> checkresponse('http://localhost:8080')
    200
    >>>
    '''
    try:
        r = requests.get(url)
        return(r.status_code)
    except Exception as e:
        print('An error occured:\n' + str(e))
        return(1)


def loadConfig(configfile):
    config = configparser.ConfigParser()
    config.read(configfile)
    protocol = config['DEFAULT']['protocol']
    host = config['DEFAULT']['host']
    port = config['DEFAULT']['port']
    indexURL = protocol + '://' + host + ':' + port + '/'
    settings = {'protocol': protocol, 'host': host, 'port': port,
                'indexURL': indexURL}
    return(settings)


if __name__ == '__main__':
    config = loadConfig('config.ini')
    run(host=config['host'], port=config['port'], reloader=True)

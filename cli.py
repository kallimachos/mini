#!/bin/python3

import configparser
import requests


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
    INDEX = loadConfig()['indexURL']
    print(checkresponse(INDEX))

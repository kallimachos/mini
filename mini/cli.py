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
    index = config['DEFAULT']['indexURL']
    print(checkresponse(index))

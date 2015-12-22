#!/bin/python3
"""Utility for loading configuration."""

import requests
try:
    import configparser
    '''
    >>> import configparser
    '''
except:
    import ConfigParser as configparser
    '''
    >>> import ConfigParser as configparser
    '''


class LoadConfig():
    """Expose configuration values from config file."""

    def __init__(self, configfile):
        """Read config file and set object values."""
        config = configparser.ConfigParser()
        config.read(configfile)
        protocol = config['DEFAULT']['protocol']
        host = config['DEFAULT']['host']
        port = config['DEFAULT']['port']
        indexURL = protocol + '://' + host + ':' + port + '/'
        self.settings = {'protocol': protocol, 'host': host, 'port': port,
                         'indexURL': indexURL}
        self.protocol = self.settings['protocol']
        self.host = self.settings['host']
        self.port = self.settings['port']
        self.indexURL = self.settings['indexURL']
        return


def checkresponse(url):
    """Confirm connection to the server."""
    try:
        r = requests.get(url)
        return(r.status_code)
    except Exception as e:
        print('An error occured:\n' + str(e))
        return(1)


if __name__ == '__main__':
    settings = LoadConfig('config.ini').settings
    print(checkresponse(settings.indexURL))

#!/bin/python3
"""Utility for loading configuration."""

import logging

import requests

try:
    import configparser
    """
    >>> import configparser
    """
except:
    import ConfigParser as configparser
    """
    Handle deprecated module name for Travis CI.

    >>> import ConfigParser as configparser
    """


class LoadConfig():
    """Expose configuration values from configfile."""

    def __init__(self, configfile):
        """Read config file and set object values."""
        config = configparser.ConfigParser()
        config.read(configfile)
        protocol = config['DEFAULT']['protocol']
        host = config['DEFAULT']['host']
        port = config['DEFAULT']['port']
        api = config['DEFAULT']['api']
        index = protocol + '://' + host + ':' + port
        api = index + '/' + api
        self.settings = {'protocol': protocol, 'host': host, 'port': port,
                         'index': index, 'api': api}
        self.protocol = self.settings['protocol']
        self.host = self.settings['host']
        self.port = self.settings['port']
        self.index = self.settings['index']
        self.api = self.settings['api']
        return


def checkresponse(url):
    """
    Confirm connection to the server.

    :param url: check response from this URL
    :type url: string
    :returns: server response code
    :rtype: int
    :example:

        >>> checkresponse('http://localhost:8080/') # doctest: +SKIP
        200
        >>> checkresponse('http://localhost:8080/404') # doctest: +SKIP
        404
        >>> checkresponse('')
        1
    """
    try:
        r = requests.get(url)
        return(r.status_code)
    except Exception as e:
        logging.error('An error occured:\n' + str(e))
        return(1)


if __name__ == '__main__':
    settings = LoadConfig('config.ini').settings
    print(checkresponse(settings.index))

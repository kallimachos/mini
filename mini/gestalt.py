#!/bin/python3

import configparser


class LoadConfig():
    def __init__(self, configfile):
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

if __name__ == '__main__':
    print(LoadConfig('config.ini').settings)

#!/bin/python3
"""Utility functions."""

import json
import logging
import sqlite3 as sql
from os import remove

import requests

from model import createDB

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


def setupTestDB(database):
    """Create test databse with example data."""
    game1 = {'ID': None, 'kind': 'game', 'name': 'Game1',
             'company': 'Company1', 'minPlayers': 1, 'maxPlayers': 4,
             'age': 10, 'length': 30, 'link': 'www.example.com', 'image': None,
             'notes': 'Fun!'}
    game2 = {'ID': None, 'kind': 'game', 'name': 'Game2',
             'company': 'Company1', 'minPlayers': 1, 'maxPlayers': 4,
             'age': 10, 'length': 30, 'link': 'www.example.com', 'image': None,
             'notes': 'Fun!'}
    game3 = {'ID': None, 'kind': 'game', 'name': 'Game3',
             'company': 'Company1', 'minPlayers': 1, 'maxPlayers': 4,
             'age': 10, 'length': 30, 'link': 'www.example.com', 'image': None,
             'notes': 'Fun!'}
    games = (game1, game2, game3)

    mini1 = {'ID': None, 'kind': 'mini', 'name': 'Mini1',
             'army': 'Orcs and Goblins', 'type': 'core', 'system': 'WFB',
             'company': 'Company1', 'quantity': 10, 'status': 'painted',
             'link': 'www.example.com', 'image': None,
             'notes': 'Fun!'}
    mini2 = {'ID': None, 'kind': 'mini', 'name': 'Mini2',
             'army': 'Orcs and Goblins', 'type': 'core', 'system': 'WFB',
             'company': 'Company1', 'quantity': 10, 'status': 'painted',
             'link': 'www.example.com', 'image': None,
             'notes': 'Fun!'}
    mini3 = {'ID': None, 'kind': 'mini', 'name': 'Mini3',
             'army': 'Orcs and Goblins', 'type': 'core', 'system': 'WFB',
             'company': 'Company1', 'quantity': 10, 'status': 'painted',
             'link': 'www.example.com', 'image': None,
             'notes': 'Fun!'}
    minis = (mini1, mini2, mini3)

    paint1 = {'ID': None, 'kind': 'paint', 'name': 'Paint1', 'color': 'green',
              'type': 'matte', 'company': 'Company1', 'quantity': 1,
              'link': 'www.example.com', 'notes': 'Fun!'}
    paint2 = {'ID': None, 'kind': 'paint', 'name': 'Paint2', 'color': 'green',
              'type': 'matte', 'company': 'Company1', 'quantity': 1,
              'link': 'www.example.com', 'notes': 'Fun!'}
    paint3 = {'ID': None, 'kind': 'paint', 'name': 'Paint3', 'color': 'green',
              'type': 'matte', 'company': 'Company1', 'quantity': 1,
              'link': 'www.example.com', 'notes': 'Fun!'}
    paints = (paint1, paint2, paint3)

    remove(database)
    createDB(database)
    con = sql.connect(database)
    with con:
        cur = con.cursor()
        cur.execute("DELETE FROM Game")
        for game in games:
            cur.execute('INSERT INTO Game VALUES (:ID, :kind, :name, \
                        :company,:minPlayers, :maxPlayers, :age, :length, \
                        :link, :image, :notes)', game)
        cur.execute("DELETE FROM Mini")
        for mini in minis:
            cur.execute('INSERT INTO Mini VALUES (:ID, :kind, :name, :army, \
                        :type, :system, :company, :quantity, :status, :link, \
                        :image, :notes)', mini)
        cur.execute("DELETE FROM Paint")
        for paint in paints:
            cur.execute('INSERT INTO Paint VALUES (:ID, :kind, :name, :color, \
                        :type, :company, :quantity, :link, :notes)', paint)

    output = []
    for line in con.iterdump():
        output.append(line)
    resp = json.dumps(output)
    return(resp)


if __name__ == '__main__':
    settings = LoadConfig('config.ini').settings
    print(checkresponse(settings.index))

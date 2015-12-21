#!/bin/python3

import gui

configfile = 'tests/config4tests.ini'
INDEX = gui.loadConfig(configfile)['indexURL']


def test_checkresponse():
    assert gui.checkresponse(INDEX) == 200


def test_loadConfig():
    settings = gui.loadConfig(configfile)
    assert settings['protocol'] == 'http'
    assert settings['host'] == 'localhost'
    assert settings['port'] == '8080'
    assert settings['indexURL'] == 'http://localhost:8080/'

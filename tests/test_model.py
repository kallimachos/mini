#!/bin/python3

import model

configfile = 'tests/config4tests.ini'
INDEX = model.loadConfig(configfile)['indexURL']


def test_checkresponse():
    assert model.checkresponse(INDEX) == 200


def test_loadConfig():
    settings = model.loadConfig(configfile)
    assert settings['protocol'] == 'http'
    assert settings['host'] == 'localhost'
    assert settings['port'] == '8080'
    assert settings['indexURL'] == 'http://localhost:8080/'

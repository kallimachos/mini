#!/bin/python3

import cli

configfile = 'tests/config4tests.ini'
INDEX = cli.loadConfig(configfile)['indexURL']


def test_checkresponse():
    assert cli.checkresponse(INDEX) == 200


def test_loadConfig():
    settings = cli.loadConfig(configfile)
    assert settings['protocol'] == 'http'
    assert settings['host'] == 'localhost'
    assert settings['port'] == '8080'
    assert settings['indexURL'] == 'http://localhost:8080/'

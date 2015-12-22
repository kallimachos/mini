#!/bin/python3

import gestalt

configfile = 'tests/config4tests.ini'
settings = gestalt.LoadConfig(configfile)


def test_loadConfig():
    assert settings.protocol == 'http'
    assert settings.host == 'localhost'
    assert settings.port == '8080'
    assert settings.indexURL == 'http://localhost:8080/'


def test_checkresponse():
    assert gestalt.checkresponse(settings.indexURL) == 200
    assert gestalt.checkresponse('failURL') == 1

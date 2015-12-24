#!/bin/python3

import gestalt

configfile = 'tests/config4tests.ini'
settings = gestalt.LoadConfig(configfile)


def test_loadConfig():
    assert settings.protocol == 'http'
    assert settings.host == 'localhost'
    assert settings.port == '8080'
    assert settings.index == 'http://localhost:8080'
    assert settings.api == 'http://localhost:8080/api'


def test_checkresponse():
    if gestalt.checkresponse(settings.index) == 200:
        assert gestalt.checkresponse(settings.index) == 200
        assert gestalt.checkresponse(settings.index + '/404') == 404
        assert gestalt.checkresponse('failURL') == 1

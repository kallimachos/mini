#!/bin/python3

import conf

configfile = 'tests/config4tests.ini'


def test_loadConfig():
    settings = conf.LoadConfig(configfile)
    assert settings.protocol == 'http'
    assert settings.host == 'localhost'
    assert settings.port == '8080'
    assert settings.indexURL == 'http://localhost:8080/'

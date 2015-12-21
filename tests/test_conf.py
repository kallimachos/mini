#!/bin/python3

import conf

configfile = 'tests/config4tests.ini'


def test_loadConfig():
    settings = conf.LoadConfig(configfile)
    assert settings.protocol == 'http'
    assert settings.host == '0.0.0.0'
    assert settings.port == '8080'
    assert settings.indexURL == 'http://0.0.0.0:8080/'

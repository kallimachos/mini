#!/bin/python3

import conf

configfile = 'tests/config4tests.ini'


def test_loadConfig():
    settings = conf.LoadConfig(configfile)
    assert settings.protocol == 'http'
    assert settings.host == '192.168.0.17'
    assert settings.port == '8080'
    assert settings.indexURL == 'http://192.168.0.17:8080/'

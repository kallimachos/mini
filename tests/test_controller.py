#!/bin/python3

import controller

configfile = 'tests/config4tests.ini'
INDEX = controller.loadConfig(configfile)['indexURL']


def test_test():
    assert controller.test() == '<h1>Test</h1>'


def test_checkresponse():
    assert controller.checkresponse(INDEX) == 200


def test_helloname():
    assert True is True


def test_loadConfig():
    settings = controller.loadConfig(configfile)
    assert settings['protocol'] == 'http'
    assert settings['host'] == 'localhost'
    assert settings['port'] == '8080'
    assert settings['indexURL'] == 'http://localhost:8080/'

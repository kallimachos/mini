#!/bin/python3

import controller
import conf

configfile = 'tests/config4tests.ini'
index = conf.LoadConfig(configfile).indexURL


def test_test():
    assert controller.test() == '<h1>Test</h1>'


def test_checkresponse():
    assert controller.checkresponse(index) == 200


def test_helloname():
    assert True is True

#!/bin/python3

import controller
import conf

configfile = 'tests/config4tests.ini'
index = conf.LoadConfig(configfile).indexURL


def test_index():
    assert controller.index() == '<h1>Index Page</h1>'


def test_helloname():
    assert controller.helloname('Brian') == '<strong>Hello Brian!</strong>'


def test_checkresponse():
    assert controller.checkresponse(index) == 200
    assert controller.checkresponse('failURL') == 1

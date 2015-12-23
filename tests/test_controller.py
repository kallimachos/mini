#!/bin/python3

import controller
import gestalt

from webtest import TestApp

configfile = 'tests/config4tests.ini'
index = gestalt.LoadConfig(configfile).indexURL

app = TestApp(controller.app)


def test_index():
    assert app.get(index).status_int == 200


def test_get_favicon():
    assert app.get(index + 'favicon.ico').status_int == 200


def test_get_css():
    assert app.get(index + 'mini.css').status_int == 200


def test_missing():
    assert app.get(index + '404').status_int == 200


def test_error():
    assert app.get(index + '500').status_int == 200


def test_helloname():
    assert app.get(index + '/hello/Brian').status_int == 200


# def test_failure():
#     assert app.get(index + 'FAILURL').status_int == 404

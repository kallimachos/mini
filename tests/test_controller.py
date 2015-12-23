#!/bin/python3

import controller
import gestalt

from webtest import TestApp

configfile = 'tests/config4tests.ini'
index = gestalt.LoadConfig(configfile).indexURL

app = TestApp(controller.app)
status = gestalt.checkresponse(index)


def test_index():
    if status == 200:
        assert app.get(index).status_int == 200


def test_get_favicon():
    if status == 200:
        assert app.get(index + 'favicon.ico').status_int == 200


def test_get_css():
    if status == 200:
        assert app.get(index + 'mini.css').status_int == 200


def test_missing():
    if status == 200:
        assert app.get(index + '404').status_int == 200


def test_error():
    if status == 200:
        assert app.get(index + '500').status_int == 200


def test_helloname():
    if status == 200:
        assert app.get(index + '/hello/Brian').status_int == 200


# def test_failure():
#     assert app.get(index + 'FAILURL').status_int == 404

#!/bin/python3

import controller
import gestalt

configfile = 'tests/config4tests.ini'
index = gestalt.LoadConfig(configfile).indexURL


# def test_index():
#     assert controller.index() == '<h1>Index Page</h1>'


def test_helloname():
    assert controller.helloname('Brian') == '<strong>Hello Brian!</strong>'

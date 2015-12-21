#!/bin/python3

import model
import gestalt

configfile = 'tests/config4tests.ini'
index = gestalt.LoadConfig(configfile).indexURL


def test_checkresponse():
    assert model.checkresponse(index) == 200
    assert model.checkresponse('failURL') == 1

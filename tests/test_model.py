#!/bin/python3

import gestalt
import model

configfile = 'tests/config4tests.ini'
index = gestalt.LoadConfig(configfile).indexURL


def test_checkresponse():
    assert model.checkresponse(index) == 200
    assert model.checkresponse('failURL') == 1

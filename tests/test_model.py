#!/bin/python3

import gestalt
import model

configfile = 'tests/config4tests.ini'
index = gestalt.LoadConfig(configfile).indexURL
status = gestalt.checkresponse(index)


def test_checkresponse():
    if status == 200:
        assert model.checkresponse(index) == 200
        assert model.checkresponse('failURL') == 1

#!/bin/python3

import gestalt
import gui

configfile = 'tests/config4tests.ini'
index = gestalt.LoadConfig(configfile).indexURL
status = gestalt.checkresponse(index)


def test_checkresponse():
    if status == 200:
        assert gui.checkresponse(index) == 200
        assert gui.checkresponse('failURL') == 1

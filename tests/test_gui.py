#!/bin/python3

import gestalt
import gui

configfile = 'tests/config4tests.ini'
index = gestalt.LoadConfig(configfile).indexURL


def test_checkresponse():
    assert gui.checkresponse(index) == 200
    assert gui.checkresponse('failURL') == 1

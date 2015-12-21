#!/bin/python3

import cli
import gestalt

configfile = 'tests/config4tests.ini'
index = gestalt.LoadConfig(configfile).indexURL


def test_checkresponse():
    assert cli.checkresponse(index) == 200
    assert cli.checkresponse('failURL') == 1

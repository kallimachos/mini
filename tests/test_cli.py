#!/bin/python3

import cli
import gestalt

configfile = 'tests/config4tests.ini'
index = gestalt.LoadConfig(configfile).indexURL
status = gestalt.checkresponse(index)


def test_checkresponse():
    if status == 200:
        assert cli.checkresponse(index) == 200
        assert cli.checkresponse('failURL') == 1

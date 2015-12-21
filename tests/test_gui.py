#!/bin/python3

import conf
import gui

configfile = 'tests/config4tests.ini'
index = conf.LoadConfig(configfile).indexURL


def test_checkresponse():
    assert gui.checkresponse(index) == 200

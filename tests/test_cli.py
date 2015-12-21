#!/bin/python3

import cli
import conf

configfile = 'tests/config4tests.ini'
index = conf.LoadConfig(configfile).indexURL


def test_checkresponse():
    assert cli.checkresponse(index) == 200

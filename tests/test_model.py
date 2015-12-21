#!/bin/python3

import model
import conf

configfile = 'tests/config4tests.ini'
index = conf.LoadConfig(configfile).indexURL


def test_checkresponse():
    assert model.checkresponse(index) == 200

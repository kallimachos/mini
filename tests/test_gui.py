#!/bin/python3

import gui


INDEX = gui.loadConfig()['indexURL']


def test_checkresponse():
    assert gui.checkresponse(INDEX) == 200

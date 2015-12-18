#!/bin/python3

import model


INDEX = model.loadConfig()['indexURL']


def test_checkresponse():
    assert model.checkresponse(INDEX) == 200

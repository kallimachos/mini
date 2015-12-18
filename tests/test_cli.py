#!/bin/python3

import cli


INDEX = cli.loadConfig()['indexURL']


def test_checkresponse():
    assert cli.checkresponse(INDEX) == 200

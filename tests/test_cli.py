#!/bin/python3

import cli
import gestalt

configfile = 'tests/config4tests.ini'
api = gestalt.LoadConfig(configfile).api
# status = gestalt.checkresponse(index)


def test_dump():
    # assert cli.dump(api) is True
    assert cli.dump('http://localhost:8080/BADAPI') is False

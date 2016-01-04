#!/bin/python3

import cli
import gestalt

api = gestalt.LoadConfig().api


def test_dump():
    # assert cli.dump(api) is True
    assert cli.dump('http://localhost:8080/BADAPI') is False

#!/bin/python3

import controller

INDEX = controller.loadConfig()['indexURL']


def test_test():
    assert controller.test() == '<h1>Test</h1>'


def test_checkresponse():
    assert controller.checkresponse(INDEX) == 200

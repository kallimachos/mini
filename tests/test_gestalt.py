#!/bin/python3

import json
import gestalt

settings = gestalt.LoadConfig()


def test_loadConfig():
    assert settings.protocol == 'http'
    assert settings.host == '0.0.0.0'
    assert settings.port == '8080'
    assert settings.index == 'http://0.0.0.0:8080'
    assert settings.api == 'http://0.0.0.0:8080/api'


def test_checkresponse():
    if gestalt.checkresponse(settings.index) == 200:
        assert gestalt.checkresponse(settings.index) == 200
        assert gestalt.checkresponse(settings.index + '/404') == 404
        assert gestalt.checkresponse('failURL') == 1


def test_setupTestDB():
    exampleDB = gestalt.setupTestDB()
    assert json.loads(exampleDB)[0] == 'BEGIN TRANSACTION;'
    assert json.loads(exampleDB)[-1] == 'COMMIT;'

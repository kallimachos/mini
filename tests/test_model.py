#!/bin/python3

import model

configfile = 'tests/config4tests.ini'
database = 'mini/test.db'
data = 'Hello'


def test_add():
    assert model.add(database, data) is None


def test_delete():
    assert model.delete(database, data) is None


def test_dump():
    assert model.dump(database) == '"DB dump test"'


def test_sqlite_version():
    assert model.sqlite_version(database) == '"SQLite version: 3.9.0"'

#!/bin/python3

import json
import model

# database = ':memory:'
database = 'mini/test.db'
gamedata = json.dumps({'kind': 'game', 'name': 'game4', 'price': 52})
minidata = json.dumps({'kind': 'mini', 'name': 'mini4', 'price': 52})
paintdata = json.dumps({'kind': 'paint', 'name': 'paint4', 'price': 52})
model.setup_test(database)


def test_add():
    assert model.add(database, gamedata) == '1'
    assert model.add(database, minidata) == '1'
    assert model.add(database, paintdata) == '1'


def test_delete():
    assert model.delete(database, gamedata) is None
    assert model.delete(database, minidata) is None
    assert model.delete(database, paintdata) is None


def test_dump():
    assert json.loads(model.dump(database))[0] == 'BEGIN TRANSACTION;'
    assert json.loads(model.dump(database))[-1] == 'COMMIT;'


def test_edit():
    assert model.edit(database, gamedata) is None
    assert model.edit(database, minidata) is None
    assert model.edit(database, paintdata) is None


def test_setup_test():
    assert json.loads(model.setup_test(database))[0] == 'BEGIN TRANSACTION;'
    assert json.loads(model.setup_test(database))[-1] == 'COMMIT;'


def test_sqlite_version():
    assert model.sqlite_version(database) == '"SQLite version: 3.9.0"'


def test_view():
    assert model.view(database, gamedata) is None
    assert model.view(database, minidata) is None
    assert model.view(database, paintdata) is None

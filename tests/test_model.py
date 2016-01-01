#!/bin/python3

import json
import model

# database = ':memory:'
database = 'mini/test.db'
model.setup_test(database)


def test_add():
    game = json.dumps({'kind': 'game', 'name': 'Game4', 'price': 52})
    mini = json.dumps({'kind': 'mini', 'name': 'Mini4', 'price': 52})
    paint = json.dumps({'kind': 'paint', 'name': 'Paint4', 'price': 52})
    assert model.add(database, game) == '1'
    assert model.add(database, mini) == '1'
    assert model.add(database, paint) == '1'


def test_delete():
    game = json.dumps({'kind': 'game', 'name': 'Game3', 'price': 52})
    mini = json.dumps({'kind': 'mini', 'name': 'Mini3', 'price': 52})
    paint = json.dumps({'kind': 'paint', 'name': 'Paint3', 'price': 52})
    assert model.delete(database, game) == '1'
    assert model.delete(database, mini) == '1'
    assert model.delete(database, paint) == '1'


def test_dump():
    assert json.loads(model.dump(database))[0] == 'BEGIN TRANSACTION;'
    assert json.loads(model.dump(database))[-1] == 'COMMIT;'


def test_edit():
    game = json.dumps({'kind': 'game', 'name': 'Game1', 'price': 52})
    mini = json.dumps({'kind': 'mini', 'name': 'Mini1', 'price': 52})
    paint = json.dumps({'kind': 'paint', 'name': 'Paint1', 'price': 52})
    assert model.edit(database, game) is None
    assert model.edit(database, mini) is None
    assert model.edit(database, paint) is None


def test_setup_test():
    assert json.loads(model.setup_test(database))[0] == 'BEGIN TRANSACTION;'
    assert json.loads(model.setup_test(database))[-1] == 'COMMIT;'


def test_sqlite_version():
    assert model.sqlite_version(database) == '"SQLite version: 3.9.0"'


def test_view():
    game = json.dumps({'kind': 'game', 'name': 'Game2', 'price': 52})
    mini = json.dumps({'kind': 'mini', 'name': 'Mini2', 'price': 52})
    paint = json.dumps({'kind': 'paint', 'name': 'Paint2', 'price': 52})
    assert model.view(database, game) == '[2, "Game2", 57]'
    assert model.view(database, mini) == '[2, "Mini2", 27]'
    assert model.view(database, paint) == '[2, "Paint2", 71]'

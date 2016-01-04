#!/bin/python3

import json
import model
from gestalt import setupTestDB


def test_add():
    game = json.dumps({'ID': None, 'kind': 'game', 'name': 'Game4',
                       'company': 'Company1', 'minPlayers': 1,
                       'maxPlayers': 4, 'age': 10, 'length': 30,
                       'link': 'www.example.com', 'image': None,
                       'notes': 'Fun!'})

    mini = json.dumps({'ID': None, 'kind': 'mini', 'name': 'Mini4',
                       'army': 'Orcs and Goblins', 'type': 'core',
                       'system': 'WFB', 'company': 'Company1', 'quantity': 10,
                       'status': 'painted', 'link': 'www.example.com',
                       'image': None, 'notes': 'Fun!'})

    paint = json.dumps({'ID': None, 'kind': 'paint', 'name': 'Paint4',
                        'color': 'green', 'type': 'matte',
                        'company': 'Company1', 'quantity': 1,
                        'link': 'www.example.com', 'notes': 'Fun!'})
    assert model.add(database, game) == '1'
    assert model.view(database, game) == '[4, "game", "Game4", "Company1", 1, \
4, 10, 30, "www.example.com", null, "Fun!"]'
    assert model.add(database, mini) == '1'
    assert model.view(database, mini) == '[4, "mini", "Mini4", \
"Orcs and Goblins", "core", "WFB", "Company1", 10, "painted", \
"www.example.com", null, "Fun!"]'
    assert model.add(database, paint) == '1'
    assert model.view(database, paint) == '[4, "paint", "Paint4", "green", \
"matte", "Company1", 1, "www.example.com", "Fun!"]'


def test_delete():
    game = json.dumps({'ID': None, 'kind': 'game', 'name': 'Game3',
                       'company': 'Company1', 'minPlayers': 1,
                       'maxPlayers': 4, 'age': 10, 'length': 30,
                       'link': 'www.example.com', 'image': None,
                       'notes': 'Fun!'})

    mini = json.dumps({'ID': None, 'kind': 'mini', 'name': 'Mini3',
                       'army': 'Orcs and Goblins', 'type': 'core',
                       'system': 'WFB', 'company': 'Company1', 'quantity': 10,
                       'status': 'painted', 'link': 'www.example.com',
                       'image': None, 'notes': 'Fun!'})

    paint = json.dumps({'ID': None, 'kind': 'paint', 'name': 'Paint3',
                        'color': 'green', 'type': 'matte',
                        'company': 'Company1', 'quantity': 1,
                        'link': 'www.example.com', 'notes': 'Fun!'})
    assert model.delete(database, game) == '1'
    assert model.view(database, game) == 'null'
    assert model.delete(database, mini) == '1'
    assert model.view(database, mini) == 'null'
    assert model.delete(database, paint) == '1'
    assert model.view(database, paint) == 'null'


def test_dump():
    assert json.loads(model.dump(database))[0] == 'BEGIN TRANSACTION;'
    assert json.loads(model.dump(database))[-1] == 'COMMIT;'


def test_edit():
    game = json.dumps({'ID': None, 'kind': 'game', 'name': 'Game1',
                       'company': 'Company1', 'minPlayers': 1,
                       'maxPlayers': 4, 'age': 10, 'length': 60,
                       'link': 'www.example.com', 'image': None,
                       'notes': 'Fun!'})

    mini = json.dumps({'ID': None, 'kind': 'mini', 'name': 'Mini1',
                       'army': 'Orcs and Goblins', 'type': 'core',
                       'system': 'WFB', 'company': 'Company1', 'quantity': 20,
                       'status': 'painted', 'link': 'www.example.com',
                       'image': None, 'notes': 'Fun!'})

    paint = json.dumps({'ID': None, 'kind': 'paint', 'name': 'Paint1',
                        'color': 'green', 'type': 'ink',
                        'company': 'Company1', 'quantity': 1,
                        'link': 'www.example.com', 'notes': 'Fun!'})
    assert model.edit(database, game) == '1'
    assert model.view(database, game) == '[1, "game", "Game1", "Company1", 1, \
4, 10, 60, "www.example.com", null, "Fun!"]'
    assert model.edit(database, mini) == '1'
    assert model.view(database, mini) == '[1, "mini", "Mini1", \
"Orcs and Goblins", "core", "WFB", "Company1", 20, "painted", \
"www.example.com", null, "Fun!"]'
    assert model.edit(database, paint) == '1'
    assert model.view(database, paint) == '[1, "paint", "Paint1", "green", \
"ink", "Company1", 1, "www.example.com", "Fun!"]'


def test_sqlite_version():
    assert json.loads(model.sqlite_version(database)).strip().split()[0:2] \
        == ['SQLite', 'version:']


def test_view():
    game = json.dumps({'ID': None, 'kind': 'game', 'name': 'Game2',
                       'company': 'Company1', 'minPlayers': 1,
                       'maxPlayers': 4, 'age': 10, 'length': 30,
                       'link': 'www.example.com', 'image': None,
                       'notes': 'Fun!'})

    mini = json.dumps({'ID': None, 'kind': 'mini', 'name': 'Mini2',
                       'army': 'Orcs and Goblins', 'type': 'core',
                       'system': 'WFB', 'company': 'Company1', 'quantity': 10,
                       'status': 'painted', 'link': 'www.example.com',
                       'image': None, 'notes': 'Fun!'})

    paint = json.dumps({'ID': None, 'kind': 'paint', 'name': 'Paint2',
                        'color': 'green', 'type': 'matte',
                        'company': 'Company1', 'quantity': 1,
                        'link': 'www.example.com', 'notes': 'Fun!'})
    assert model.view(database, game) == '[2, "game", "Game2", "Company1", 1, \
4, 10, 30, "www.example.com", null, "Fun!"]'
    assert model.view(database, mini) == '[2, "mini", "Mini2", \
"Orcs and Goblins", "core", "WFB", "Company1", 10, "painted", \
"www.example.com", null, "Fun!"]'
    assert model.view(database, paint) == '[2, "paint", "Paint2", "green", \
"matte", "Company1", 1, "www.example.com", "Fun!"]'

# Set up DB for test run
# database = ':memory:'
database = 'mini/test.db'
setupTestDB(database)

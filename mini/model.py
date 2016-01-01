#!/bin/python3
"""Model for mini."""

import json
import sqlite3 as sql

database = 'sqlite.db'


def add(database, data):
    """Add an item to the DB."""
    item = json.loads(data)
    kind = item['kind']
    con = sql.connect(database)
    with con:
        cur = con.cursor()
        if kind == 'game':
            entry = (item['name'], item['price'])
            cur.execute("INSERT INTO Game (name, price) VALUES(?,?)", entry)
        elif kind == 'mini':
            entry = (item['name'], item['price'])
            cur.execute("INSERT INTO Mini (name, price) VALUES(?,?)", entry)
        elif kind == 'paint':
            entry = (item['name'], item['price'])
            cur.execute("INSERT INTO Paint (name, price) VALUES(?,?)", entry)
        resp = json.dumps(cur.rowcount)
        # resp = json.dumps(cur.lastrowid)
        return(resp)


def delete(database, data):
    """Delete an item from the DB."""
    item = json.loads(data)
    kind = item['kind']
    entry = (item['name'],)
    con = sql.connect(database)
    with con:
        cur = con.cursor()
        if kind == 'game':
            cur.execute("DELETE FROM Game WHERE name = ?", entry)
        elif kind == 'mini':
            cur.execute("DELETE FROM Mini WHERE name = ?", entry)
        elif kind == 'paint':
            cur.execute("DELETE FROM Paint WHERE name = ?", entry)
        resp = json.dumps(cur.rowcount)
        return(resp)


def dump(database):
    """
    Return a raw dump of the DB.

    :returns: a raw dump of the DB
    :rtype: JSON
    """
    con = sql.connect(database)
    output = []
    for line in con.iterdump():
        output.append(line)
    resp = json.dumps(output)
    return(resp)


def edit(database, data):
    """Edit an item in the DB."""
    # cursor.execute('''UPDATE users SET phone = ? WHERE id = ? ''',
    #                (newphone, userid))
    pass


def sqlite_version(database):
    """Return the SQLite version of a database."""
    con = sql.connect(database)
    with con:
        cur = con.cursor()
        cur.execute('SELECT SQLITE_VERSION()')
        data = cur.fetchone()
        resp = json.dumps('SQLite version: %s' % data)
        return(resp)


def setup_test(database):
    """Drop and recreate the tables in a database for testing."""
    games = (
        ('Game1', 52),
        ('Game2', 57),
        ('Game3', 90),
    )
    minis = (
        ('Mini1', 42),
        ('Mini2', 27),
        ('Mini3', 20),
    )
    paints = (
        ('Paint1', 26),
        ('Paint2', 71),
        ('Paint3', 30),
    )
    con = sql.connect(database)
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Game")
        cur.execute("""CREATE TABLE Game
                    (Id INTEGER PRIMARY KEY,
                    Name TEXT NOT NULL,
                    Price INT)""")
        cur.executemany("INSERT INTO Game (Name, Price) VALUES(?, ?)", games)
        cur.execute("DROP TABLE IF EXISTS Mini")
        cur.execute("""CREATE TABLE Mini
                    (Id INTEGER PRIMARY KEY,
                    Name TEXT NOT NULL,
                    Price INT)""")
        cur.executemany("INSERT INTO Mini (Name, Price) VALUES(?, ?)", minis)
        cur.execute("DROP TABLE IF EXISTS Paint")
        cur.execute("""CREATE TABLE Paint
                    (Id INTEGER PRIMARY KEY,
                    Name TEXT NOT NULL,
                    Price INT)""")
        cur.executemany("INSERT INTO Paint (Name, Price) VALUES(?, ?)", paints)
    output = []
    for line in con.iterdump():
        output.append(line)
    resp = json.dumps(output)
    return(resp)


def view(database, data):
    """View an item in the DB."""
    item = json.loads(data)
    kind = item['kind']
    entry = (item['name'],)
    con = sql.connect(database)
    with con:
        cur = con.cursor()
        if kind == 'game':
            cur.execute("SELECT * FROM Game WHERE name = ?", entry)
        elif kind == 'mini':
            cur.execute("SELECT * FROM Mini WHERE name = ?", entry)
        elif kind == 'paint':
            cur.execute("SELECT * FROM Paint WHERE name = ?", entry)
        resp = json.dumps(cur.fetchone())
        return(resp)


if __name__ == '__main__':
    # These statements are for testing only. Remove all but the version
    # line for production
    database = 'test.db'
    setup_test(database)
    print(json.loads(sqlite_version(database)) + '\n')
    game = json.dumps({'kind': 'game', 'name': 'Game2', 'price': 52})
    mini = json.dumps({'kind': 'mini', 'name': 'Mini2', 'price': 52})
    paint = json.dumps({'kind': 'paint', 'name': 'Paint2', 'price': 52})
    print(view(database, game))
    print(view(database, mini))
    print(view(database, paint))
    for line in json.loads(dump(database)):
        print(line)

#!/bin/python3
"""Model for mini."""

import json
import sqlite3 as sql


def add(database, data):
    """Add an item to the DB."""
    pass


def delete(database, data):
    """Delete an item from the DB."""
    pass


def dump(database):
    """
    Return a raw dump of the DB.

    :returns: a raw dump of the DB
    :rtype: JSON
    """
    resp = json.dumps('DB dump test')
    return(resp)


def sqlite_version(database):
    """Return the SQLite version of a database."""
    con = sql.connect(database)
    with con:
        cur = con.cursor()
        cur.execute('SELECT SQLITE_VERSION()')
        data = cur.fetchone()
        resp = json.dumps('SQLite version: %s' % data)
        return(resp)


if __name__ == '__main__':
    print(json.loads(sqlite_version('test.db')))

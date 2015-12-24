#!/bin/python3
"""Model for mini."""

import json


def create():
    """Create a DB."""
    pass


def add():
    """Add an item to the DB."""
    pass


def dump():
    """
    Return a raw dump of the DB.

    :returns: a raw dump of the DB
    :rtype: JSON
    """
    resp = json.dumps('This is a string that represents a dumped DB')
    return(resp)


if __name__ == '__main__':
    print(dump())

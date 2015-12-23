#!/bin/python3
"""Model for mini."""

import requests

import gestalt


def checkresponse(url):
    """Confirm connection to the server."""
    try:
        r = requests.get(url)
        return(r.status_code)
    except Exception as e:
        print('An error occured:\n' + str(e))
        return(1)


if __name__ == '__main__':
    index = gestalt.LoadConfig('config.ini').indexURL
    print(checkresponse(index))

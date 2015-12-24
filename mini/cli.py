#!/bin/python3
"""CLI client for interacting with the mini REST API."""

import json

import requests

import gestalt


def callapi(api, method, call):
    """
    Call the mini REST API.

    :param api: the API endpoint root
    :type api: string
    :param call: the function call
    :type api: string
    :param method: the HTTP method
    :type api: string
    :returns: API response
    :rtype: JSON
    """
    if method == 'get':
        try:
            r = requests.get(api + '/' + call)
        except Exception as e:
            return(e, False)
        try:
            resp = json.loads(r.text)
            return(resp, True)
        except ValueError as e:
            return(e, False)
    elif method == 'put':
        pass
    elif method == 'post':
        pass
    elif method == 'delete':
        pass
    return(r.status_code)


def dump(api):
    """
    Print a raw dump of the DB.

    :param api: the API endpoint root
    :type api: string
    :example:

        >>> dump('http://localhost:8080/api')  # doctest: +SKIP
        This is a string that represents a dumped DB
        True
        >>> dump('http://localhost:8080/BADAPI')  # doctest: +SKIP
        Expecting value: line 1 column 1 (char 0)
        False
    """
    output = callapi(api, 'get', 'dump')
    print(output[0])
    return(output[1])


def endpoints(api):
    """
    Print a list of API endpoints.

    :param api: the API endpoint root
    :type api: string
    """
    output = callapi(api, 'get', 'endpoints')
    for endpoint in output[0]:
        print(endpoint[0] + ' ' + endpoint[1])


if __name__ == '__main__':
    api = gestalt.LoadConfig('config.ini').api
    print('Making API requests to ' + api)
    dump(api)
    endpoints(api)

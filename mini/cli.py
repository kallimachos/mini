#!/bin/python3
"""CLI client for interacting with the mini REST API."""

import json
import os
import sys
import time

import requests

import gestalt

# set api url
api = gestalt.LoadConfig().api
menu_actions = {}


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


def dump():
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
    print("\n9. Main Menu")
    print("Q. Quit\n")
    choice = input(">>  ")
    exec_menu(choice)


def endpoints():
    """
    Print a list of API endpoints.

    :param api: the API endpoint root
    :type api: string
    """
    output = callapi(api, 'get', 'endpoints')
    for endpoint in output[0]:
        print(endpoint[0] + ' ' + endpoint[1])
    print("\n9. Main Menu")
    print("Q. Quit\n")
    choice = input(">>  ")
    exec_menu(choice)


def exec_menu(choice):
    ch = choice.upper()
    os.system('clear')
    if ch == '':
        menu_actions['menu']()
    else:
        try:
            print('Making API requests to ' + api + '\n')
            menu_actions[ch]()
        except KeyError:
            os.system('clear')
            print("Invalid selection, please try again.\n")
            time.sleep(2)
            menu_actions['menu']()
    return


def finish():
    """
    Quit the program.
    """
    os.system('clear')
    sys.exit(0)


def menu():
    """
    Display menu and loop until user exit.
    """
    os.system('clear')
    print('Making API requests to ' + api)
    menu ="""
1. Dump - Print database dump
2. Endpoints - print endpoints
Q. Quit
           """
    print(menu)
    choice = input(">> ")
    exec_menu(choice)
    return

# Main definition - constants
menu_actions = {
        'menu': menu,
        '1': dump,
        '2': endpoints,
        '9': menu,
        'Q': finish,
    }

if __name__ == '__main__':
    menu()

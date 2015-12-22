#!/bin/python3

import gestalt
import requests


def hi(firstname, lastname):
    '''
    This function returns a greeting to the named person.

    :param firstname: first name
    :param lastname: last name
    :type firstname: string
    :type lastname: string
    :returns: a greeting to the named person
    :rtype: string
    :example:

        >>> hi('Brian', 'Moss')
        'Hi Brian Moss!'
    '''

    response = "Hi " + firstname + " " + lastname + "!"
    return(response)


def checkresponse(url):
    try:
        r = requests.get(url)
        return(r.status_code)
    except Exception as e:
        print('An error occured:\n' + str(e))
        return(1)


if __name__ == '__main__':
    index = gestalt.LoadConfig('config.ini').indexURL
    print(checkresponse(index))

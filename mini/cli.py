#!/bin/python3

import gestalt
import requests


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

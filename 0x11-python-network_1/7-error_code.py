#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response.

"""
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)
    status_code = response.status_code
    if status_code >= 400:
        print("Error code: {}".format(status_code))

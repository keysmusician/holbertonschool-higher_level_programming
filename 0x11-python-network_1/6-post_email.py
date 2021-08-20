#!/usr/bin/python3
"""
Sends a POST request to a URL with an email as a parameter, and displays the
body of the response.

"""
import requests
import sys

from requests.api import post


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    post_data = {"email": email}
    response = requests.post(url, post_data)
    print(response.text)

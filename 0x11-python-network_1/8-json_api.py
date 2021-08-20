#!/usr/bin/python3
"""
Sends a POST request with a letter as a parameter.

"""
import requests
import sys

from requests import exceptions


if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"

    try:
        letter = sys.argv[2]
    except IndexError:
        letter = ""

    post_data = {"q": letter}
    response = requests.post(url, post_data)

    try:
        decoded = response.json()
        print("[{}] {}".format(decoded["id"], decoded["name"]))
    except:
        print("Not a valid JSON")

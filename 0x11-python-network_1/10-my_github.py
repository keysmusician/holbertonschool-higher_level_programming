#!/usr/bin/python3
"""Uses the GitHub API to display your GitHub ID."""
import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    credentials = HTTPBasicAuth(username, password)
    url = "https://api.github.com/user/"
    response = requests.get(url, auth=credentials)
    content = response.json()
    print(content.get("id"))

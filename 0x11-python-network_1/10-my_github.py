#!/usr/bin/python3
"""Uses the GitHub API to display your GitHub ID."""
from requests import get
from requests.auth import HTTPBasicAuth
from sys import argv
if __name__ == "__main__":
    url = 'https://api.github.com/user'
    r = get(url, auth=HTTPBasicAuth(argv[1], argv[2]))
    try:
        info = r.json()
        print(info['id'])
    except:
        print('None')

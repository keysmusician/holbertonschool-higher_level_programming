#!/usr/bin/python3
"""Prints 10 commits."""
import requests
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    repo = argv[2]
    url = "http://api.github.com/repos/{}/{}/commits".format(user, repo)
    response = requests.get(url)
    commits = response.json()
    for idx, commit in enumerate(commits):
        if idx == 10:
            break
        print("{}: {}".format(
            commit.get("sha"), commit.get("author").get("name"))
        )

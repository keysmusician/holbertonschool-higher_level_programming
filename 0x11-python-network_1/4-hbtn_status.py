#!/usr/bin/python3
"""Fetches a URL."""
import requests


response = requests.get("https://intranet.hbtn.io/status")
text = response.text
print(
    """\
Body response:
\t- type: {}
\t- content: {}\
""".format(type(text), text)
)

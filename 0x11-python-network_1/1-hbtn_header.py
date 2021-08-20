#!/usr/bin/python3
"""
Sends a request to a given URL and displays the value of the X-Request-Id
variable found in the header of the response.

"""
import sys
import urllib.request

url = sys.argv[1]

with urllib.request.urlopen(url) as request:
    print(request.getheader('X-Request-Id'))

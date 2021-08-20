#!/usr/bin/python3
"""
Sends a POST request to a URL with an email as a parameter, and displays the
body of the response (decoded in utf-8).

"""
import sys
from urllib.request import Request, urlopen
from urllib.parse import urlencode


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    clientdata = {'email': email}
    urldata = urlencode(clientdata).encode('ascii')
    request = Request(url, urldata)

    with urlopen(request) as response:
        print(response.read().decode('utf-8'))

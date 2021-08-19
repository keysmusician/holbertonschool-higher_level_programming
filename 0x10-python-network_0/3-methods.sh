#!/bin/bash
# Take a URL and display all HTTP methods the server will accept
curl -sIX OPTIONS 0:5000 | grep Allow: | cut -d " " -f 2-

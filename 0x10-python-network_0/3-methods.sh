#!/bin/bash
# Take a URL and display all HTTP methods the server will accept
curl -sIX OPTIONS "$1" | grep Allow: | cut -d " " -f 2-

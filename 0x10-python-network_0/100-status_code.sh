#!/bin/bash
# Prints HTTP status code with only curl
curl -so /dev/null -w "%{http_code}" "$1"

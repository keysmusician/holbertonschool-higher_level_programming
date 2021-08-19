#!/bin/bash
# Displays the size of the body of the response to an HTTP request
curl -s "$1" | wc -c

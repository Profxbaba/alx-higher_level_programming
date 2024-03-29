#!/bin/bash
# This script takes a URL as input, sends a GET request to the URL using curl in silent mode, displays the body of the response if the status code is 200
curl -sL -w "%{http_code}" "$1" -o /dev/null | { [ "$(tail -c 3)" == "200" ] && curl -sL "$1"; }

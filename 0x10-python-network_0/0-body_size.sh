#!/bin/bash
#Bash script that takes in a URL, send a request to an URL with curl, and displays the size of the body of the response
curl -s "$1" | wc -c

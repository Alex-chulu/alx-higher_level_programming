#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response

url=$1;
response=$(curl -s -w "\n%{size_download}" $url);size=$(echo $response | tail -n1);
echo "The size of the body of the response is $size bytes."

#!/bin/bash

url=$1;
response=$(curl -s -w "\n%{size_download}" $url);size=$(echo $response | tail -n1);
echo "The size of the body of the response is $size bytes."

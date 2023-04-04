#!/usr/bin/python3

import urllib.request
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')#data should be bytes

    with urllib.request.urlopen(url, data) as response:
        html = response.read()
        print(html.decode('utf-8'))

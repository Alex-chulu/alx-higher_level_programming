#!/usr/bin/python3

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email':sys.argv[2]}
    
    data = urllib.parse.urlencode(email)
    dat = data.encode('ascii')

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))

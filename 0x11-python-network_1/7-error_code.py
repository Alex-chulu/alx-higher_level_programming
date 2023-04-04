#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to 
the URL and displays the body of the response.
"""
import sys
import requests

if __name__ == '__main__':
    url = input("Enter a URL: ")
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.content)

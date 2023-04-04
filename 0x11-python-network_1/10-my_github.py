#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
import sys

username = sys.argv[1]
password = sys.argv[2]

url = f"https://api.github.com/user"

response = requests.get(url, auth=(username, password))
print(response.json()["id"])

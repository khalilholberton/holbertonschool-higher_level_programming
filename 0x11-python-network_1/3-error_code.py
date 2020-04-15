#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).and manage
urllib.error.HTTPError exceptions and print: Error code: followed by
the HTTP status code
"""
import urllib.request
import urllib.parse
from urllib import error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
            print(the_page.decode("UTF-8"))
    except error.HTTPError as e:
        print("{}".format("Error code:"), e.getcode())

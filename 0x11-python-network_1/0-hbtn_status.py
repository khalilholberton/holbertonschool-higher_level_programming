#!/usr/bin/python3
# Python  Script that fetch a url

import urllib.request

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status/"
    with urllib.request.urlopen(url) as r:
        response = r.read()
        print("Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(response.decode("utf-8")))

#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys

if __name__ == "__main__":
    try:
        q = sys.argv[1]
    except:
        q =""
    try:
        r = requests.post('http://0.0.0.0:5000/search_user', data = {"q": q})
        r = r.json()
        if r.get("id") is None or r.get("name") is None:
            print("No result")
        else:
            print("[{}] <{}>".format(r.get("id"), r.get("name")))
    except ValueError:
        print("Not a valid JSON")

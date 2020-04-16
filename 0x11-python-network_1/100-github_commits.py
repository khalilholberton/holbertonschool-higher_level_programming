#!/usr/bin/python3

# Python Script
import requests as req
from sys import argv


if __name__ == "__main__":
    r = req.get('https://api.github.com/repos/{}/{}/commits'
                .format(argv[2], argv[1]))
    res_data = r.json()
    counter = 0
    for commit in res_data:
        name = commit.get("commit").get("author").get("name")
        sha = commit.get("sha")

        print("{}: {}".format(sha, name))
        counter += 1
        if counter > 9:
            break

#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    sym = "__"
    for x in (dir(hidden_4)):
        if sym not in x:
            print(x)

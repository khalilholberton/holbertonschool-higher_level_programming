#!/usr/bin/python3
'''
adds all arguments to a Python list, and then save them to a file
'''
import json
from sys import argv


save_json = __import__('7-save_to_json_file').save_to_json_file
load_json = __import__('8-load_from_json_file').load_from_json_file

myfile = 'add_item.json'

try:
    myl = load_json(myfile)
except:
    myl = []

myl += argv[1:]
save_json(myl, myfile)

#!/usr/bin/python3

import os

def walk(path):
    for root, dirs, files in os.walk(path):
        for f in files:
            print(os.path.join(root, f))

cwd = os.getcwd()
walk(cwd)

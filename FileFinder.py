#!/usr/bin/env python
# -*- coding: utf8 -*-
"""This application finds files in a sub-directory tree.
"""

APP_NAME = "FileFinder"
__version__ = "0.1"
__author__ = "Jaume Martin"


import argparse
import os
import sys

from functools import partial


def discart(f, ext):
    """It returns if a file `f` ends with `ext`
    """
    return f.endswith(ext)


def walk_and_find(path, string, ext):
    """It walk through the whole sub-directory which its root is `path`. If the `string`is in one of the files
    the functions print the file name.
    """
    file_found = False
    for root, directories, files in os.walk(path):
        for f in filter(partial(discart, ext=ext), files):
            with open(os.path.join(root, f)) as file:
                content = file.read()
                if string in content:
                    print("File found: {}".format(os.path.join(root, f)))
                    file_found = True
    if not file_found:
        print("File not found. :(")


def main(path, string, ext):
    """It is just a wrapper
    """
    walk_and_find(path, string, ext)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog=APP_NAME, description="Find the missed file")
    parser.add_argument("--string", required=True, help="String to find")
    parser.add_argument("--path", required=True, help="Path where start finding")
    parser.add_argument("--ext", default=".txt", help="The files extension")
    args = parser.parse_args()

    string = args.string
    path = args.path
    ext = args.ext
    
    print("{} is looking for files *{} which contains '{}'".format(APP_NAME, ext, string))
    
    sys.exit(main(path, string, ext))
    

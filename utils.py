"""
Minimum Python version 3.x
Using Python version 3.9.5
"""

import os

def str_split(string: str):
    return [char for char in string]


def fsize(target: str):  # File/folder size
    if is_file(target) or is_dir(target):
	    return os.stat(target).st_size
    return None


def fmdate(target: str):  # Date last modified
    if is_file(target) or is_dir(target):
	    return os.path.getmtime(target)
    return None


def is_dir(target: str):
	return os.path.isdir(target)


def is_file(target: str):
	return os.path.isfile(target)


def abspath(target: str):
    if is_file(target) or is_dir(target):
        return os.path.abspath(target)
    return ""


def get_path(from_filename: str, path_format: str = "lunix"):
    curdir = ""

    if path_format in ("unix", "linux", "lunix"):        
        curdir = os.path.realpath(from_filename).replace("\\", "/")
        curdir = curdir.split("/")
        curdir.pop()
        curdir = "/".join(curdir)

    elif path_format in ("nt", "windows", "win"):
        curdir = curdir.split("\\")
        curdir.pop()
        curdir = "\\".join(curdir)

    return curdir

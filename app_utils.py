"""
Minimum Python version 3.x
Using Python version 3.9.5
"""

import os
from datetime import datetime
import socket
from time import ctime
import pyunpack
import re
import xtarfile as tarfile


def str_split(string: str):
    return [char for char in string]


def is_dir(target: str):
    return os.path.isdir(target)


def is_file(target: str):
    return os.path.isfile(target)


def fsize(target: str):  # File/folder size
    if is_file(target) or is_dir(target):
        return os.stat(target).st_size
    return None


def fmdate(target: str):  # Date last modified
    if is_file(target) or is_dir(target):
        return os.path.getmtime(target)
    return None


def fcdate(target: str):  # Date creation
    if is_file(target) or is_dir(target):
        return ctime(fmdate(target))
    return None


def fname(target: str):
    if is_file(target):
        name, ext = os.path.splitext(target)
        return name
    return ""


def fext(target: str):
    if is_file(target):
        name, ext = os.path.splitext(target)
        return ext[1::]  # Remove the leading dot
    return ""


def is_xml(target: str):
    if is_file(target) and "xml" in fext(target):  # Verify file's extension
        with open(target, "r") as tmp_xml:
            for line in tmp_xml:
                if re.match(r"(<\?xml version=\".+\" encoding=\".+\"\?>)", line.strip()):  # Verify header
                    return True
    return False


def is_pdf(target: str):
    if is_file(target) and fext(target) == "pdf":  # Verify file's extension
        tmp_pdf = open(target, "rb")
        pdf = tmp_pdf.read(8).decode("utf-8")
        if re.match(r"^\%PDF\-\d", pdf.strip()):  # Verify header
            return True
    return False


def frecent(target: str):
    ts = datetime.fromtimestamp(fmdate(target))
    y = int(ts.strftime("%Y"))
    mm = int(ts.strftime("%m"))
    d = int(ts.strftime("%d"))
    
    h = int(ts.strftime("%H"))
    mn = int(ts.strftime("%I"))
    s = int(ts.strftime("%S"))
    
    then = datetime(y, mm, d, h, mn, s)
    now  = datetime.now()
    
    duration = now - then
    seconds = duration.total_seconds()
    days = datetime.fromtimestamp(seconds).strftime("%d")

    return int(days) <= 1


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


def ip():
  h = socket.gethostname()
  ip = socket.gethostbyname(h)
  return ip


def un7zip(target: str, destination: str):  # Requires pyunpack and patool installed
    if is_file(target) and fext(target) == "7z":
        try:
            pyunpack.Archive(target).extractall(destination)
        except Exception as e:
            print(e)


def untar(target: str, destination: str):  # Requires xtarfile installed
    if is_file(target) and fext(target) == "tar":
        try:
            with tarfile.open(target) as tar:
                tar.extractall(destination)
                tar.close()
        except Exception as e:
            print(e)

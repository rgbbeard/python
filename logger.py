"""
Minimum Python version 3.x
Using Python version 3.9.5
Author - Davide - 26/10/2021
Git - github.com/rgbbeard
"""

from os import (system, path)
from re import match as matches
from time import strftime
from app_utils import get_path

class Logger:
    def __init__(self, filename: str = "logfile.log"):
        if not matches(r"\\|\/", filename):
            filename = get_path(filename) + "/" + filename

        self.__filename = filename
        self.__logfile = open(filename, "a")

    def __del__(self):
        if self.__logfile != None:
            self.__logfile.close()
            self.__logfile = None

    def __get_time(self):
        return str("[" + strftime("%H:%M:%S  %d/%m/%Y") + "]")

    def __reopen(self):
        self.__logfile = open(self.__filename, "a")

    def save(self, message: str):
        if self.__logfile != None:
            self.__logfile.write(message)
            self.__logfile.close()
            self.__logfile = None

    def log(self, message):
        if self.__logfile == None:
            self.__reopen()

        message = f"[CONSOLE] {message}\n"
        message = self.__get_time() + str(message)

        self.save(message)

    def inform(self, message):
        if self.__logfile == None:
            self.__reopen()
   
        message = f"[INFO] {message}\n"
        message = self.__get_time() + str(message)

        self.save(message)

    def warn(self, message):
        if self.__logfile == None:
            self.__reopen()

        message = f"[WARNING] {message}\n"
        message = self.__get_time() + str(message)

        self.save(message)

    def error(self, message):
        if self.__logfile == None:
            self.__reopen()
            
        message = f"[ERROR] {message}\n"
        message = self.__get_time() + str(message)

        self.save(message)

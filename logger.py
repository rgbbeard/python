"""
Minimum Python version 3.x
Using Python version 3.9.5
Author - Davide - 26/10/2021
Git - github.com/rgbbeard
"""

from os import (system, path)
from time import strftime

class Logger:
    def __init__(self, type: str = "l", message: str = "", filename: str = "logfile.log"):
        abspath = os.path.realpath(__file__)
        self.__logfile = open(filename, "a")

        if type == "l":
            self.__log(message)
        elif type == "i":
            self.__inform(message)
        elif type == "w":
            self.__warn(message)
        elif type == "e":
            self.__error(message)

    def __del__(self):
        self.__logfile.close()

    def __get_time(self):
        return str("[" + strftime("%H:%M:%S  %d/%m/%Y") + "]")

    def __save(self, message: str):
        self.__logfile.write(message)

    def __log(self, message):
        message = f"[CONSOLE] {message}\n"
        message = self.__get_time() + str(message)

        self.__save(message)

    def __inform(self, message):
        message = f"[INFO] {message}\n"
        message = self.__get_time() + str(message)

        self.__save(message)

    def __warn(self, message):
        message = f"[WARNING] {message}\n"
        message = self.__get_time() + str(message)

        self.__save(message)

    def __error(self, message):
        message = f"[ERROR] {message}\n"
        message = self.__get_time() + str(message)

        self.__save(message)

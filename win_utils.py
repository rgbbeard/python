"""
Minimum Python version 3.x
Using Python version 3.9.5
"""

from app_utils import (fmdate, fname, fext, frecent, is_file, is_dir)
from os import system as cmd
import pyunpack


ROOT = "s:/dati_cliente/municipia"
SFTP = "d:/utentisftp/municipia"


def fmove_local(target: str, destination: str):
	if (is_file(target) or is_dir(target)) and is_dir(destination):
		cmd(f'move ./"{target}" "{destination}"')


def frename_local(target: str, new_name: str):
	if is_file(target) or is_dir(target):
		cmd(f"rename {target} {new_name}")


def unzip(target: str, destination: str):  # Requires pyunpack and patool installed
	if is_file(target) and fext(target) == "7z":
		try:
			pyunpack.Archive(target).extractall(destination)
		except Exception as e:
			print(e)

"""
Minimum Python version 3.x
Using Python version 3.9.5
"""

from PIL import Image  # Requires Pillow installed
from os import (listdir, chdir)
from sys import argv
from app_utils import (is_file, fext, fname)

startdir = "."
if not (not argv[1]):
	startdir = argv[1].replace("/", "\\")

destdir = startdir
if not (not argv[2]):
	destdir = argv[2].replace("/", "\\")

chdir(startdir)

for file in listdir():
	if is_file(file) and fext(file).lower() in ["jpg", "jpeg"]:
		tmp_img = Image.open(f"{startdir}\\{file}")
		new_img = tmp_img.convert("RGB")
		pdf_name = fname(file) + ".pdf"
		new_img.save(f"{destdir}\\{pdf_name}")

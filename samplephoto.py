# SamplePhoto
# Sample random photos from a specified root directory and displays them
# Author: Mirko Salaris

import os
from os.path import join
import random
import argparse
import pathlib
import shutil
from datetime import date

parser = argparse.ArgumentParser(
																prog='SamplePhoto',
																description='Sample random photos from a specified root directory and copy them to a destination folder')

parser.add_argument("--path",
										help="The root path from which to choose photos",
										type=pathlib.Path,
										default='{REDACTED}')
parser.add_argument("-n", "--number",
										help="The number of photos to sample",
										type=int,
										default=10)
parser.add_argument("--dest",
										help="The destination path where to copy the selected photos",
										type=pathlib.Path,
										default='{REDACTED}')


args = parser.parse_args()
if not os.path.exists(args.dest):
    os.makedirs(args.dest)

destination = os.path.join(args.dest, str(date.today()))
if not os.path.exists(destination):
	os.makedirs(destination)

def list_files_recursive(path='.', filetypes=(".png", ".jpg", ".bmp", ".jpeg")):
	full_list = []
	for entry in os.listdir(path):
		full_path = os.path.join(path, entry)
		if os.path.isdir(full_path):
			full_list.extend(list_files_recursive(full_path))
		elif full_path.lower().endswith(filetypes):
			full_list.append(full_path)
	return full_list

photos = list_files_recursive(args.path)

log_file = os.path.join(destination, "log.txt")
for n in range(args.number):
	choice = random.choice(photos)
	with open(log_file,'a') as f:
		f.write(choice)
	shutil.copy2(choice, destination)


## Original code ##
# Print a random file from c:\folder1\folder2\image_folder
""" import os
from os.path import isfile, join
import random

path = join("c:\\", "folder1", "folder2", "image_folder")
filetypes = tuple(".png", ".jpg", ".bmp")  # works with .endswith()

files = [join(path, f) for f in os.listdir(path) if isfile(join(path, f))]
files = [f for f in files if f.endswith(filetypes)]

choice = random.choice(files)
print(choice)

# Requires Pillow to be installed with pip
# https://pypi.org/project/Pillow/
from PIL import Image

img = Image.open(choice)
img.show() """
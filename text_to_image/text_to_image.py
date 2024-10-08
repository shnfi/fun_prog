#!/usr/bin/python3

import os
from bs4 import BeautifulSoup
import requests
from random import randint
import platform

text = input("enter your text > ")

for i in text :
	if i == " " : text = text.replace(i, "+")

url = f"https://www.google.com/search?q={text}&source=lnms&udm=2"

res = requests.get(url).text
parsed_url = BeautifulSoup(res, "html.parser")

images_count = len(parsed_url.find_all("img"))

random_image_index = randint(0, images_count)

image_url = parsed_url.find_all("img")[random_image_index]["src"]

if platform.system() == "Linux" or "Darwin" :
	os.system(f"firefox {image_url}")
elif platform.system() == "Windows" :
	os.system(f"start firefox {image_url}")

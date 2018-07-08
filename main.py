#!/usr/bin/env python

from PIL import Image


def getRGBArray(image_path):
	im = Image.open(image_path)
	width, height = im.size
	rgb_arr = [[(0,0,0) for i in range(width)] for i in range(height)]

	for i in range(height):
		for j in range(width):
			# Reverse width/height for getpixel
			rgb_arr[i][j] = im.getpixel((j,i))

	return rgb_arr


def main():
	image_path = raw_input("Enter the path to an image: ")
	keyword = raw_input("Enter a keyword: ")

	arr = getRGBArray(image_path)

if __name__ == "__main__":
	main()

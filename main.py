#!/usr/bin/env python

from PIL import Image
from utils.image_utils import getRGBArray, getAverageColour


def main():
	image_path = raw_input("Enter the path to an image: ")
	keyword = raw_input("Enter a keyword: ")

	# For testing :-)
	# image_path = "hotdog.jpg"

	im = Image.open(image_path)
	rgb = getAverageColour(im)

	avg_colour_img = Image.new('RGB', (100,100), color=rgb)
	avg_colour_img.show()


if __name__ == "__main__":
	main()

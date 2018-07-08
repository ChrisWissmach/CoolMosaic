#!/usr/bin/env python

from PIL import Image
import argparse
from utils.image_utils import getRGBArray, getAverageColour


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("file", help="image to create a mosaic for")
	parser.add_argument("keyword", help="keyword of images that make up your mosaic")
	args = parser.parse_args()

	# For testing :-)
	# image_path = "hotdog.jpg"

	im = Image.open(args.file)
	rgb = getAverageColour(im)

	avg_colour_img = Image.new('RGB', (100,100), color=rgb)
	avg_colour_img.show()


if __name__ == "__main__":
	main()

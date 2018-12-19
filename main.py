#!/usr/bin/env python

from PIL import Image
import argparse
from utils.image_utils import getRGBArray, getAverageColour, getMostAppropriateImage
from utils.image_crawler import crawlImages


def makeMosaic(im, keyword, tile_size, group_size, file_name, verbose=False):
	orig_width, orig_height = im.size
	mosaic_images = crawlImages(keyword, verbose)

	images_arr= []

	if (verbose):
		print "Creating image database"
	for i in mosaic_images:
		i2 = Image.open(i).resize((tile_size, tile_size))
		images_arr.append((getAverageColour(i2), i2))

	new_width = orig_width * tile_size / group_size
	new_height = orig_height * tile_size / group_size

	x1 = x2 = 0
	y1 = y2 = tile_size

	mosaic = Image.new('RGB', (new_width, new_height), 0)

	processed = 1

	for i in range(group_size, orig_height, group_size):
		x1 = 0
		x2 = tile_size
		for j in range(group_size, orig_width, group_size):
			if (verbose):
				processed += 1
				if (processed % 100 == 0):
					print "Processing"
			best_im = getMostAppropriateImage(getAverageColour(im.crop((j - group_size, i - group_size, j, i))), images_arr)
			mosaic.paste(best_im.resize((tile_size, tile_size)), (x1, y1))
			x1 = x2 + 1
			x2 += tile_size + 1
		y1 = y2 + 1
		y2 += tile_size + 1

	mosiac_file_name = file_name.split('.')[0] + '_mosaic.png'

	mosaic.save(mosiac_file_name, 'PNG')

	mosaic.show()

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("file", help="image to create a mosaic for")
	parser.add_argument("keyword", help="keyword of images that make up your mosaic")
	parser.add_argument("-v", "--verbose", action="store_true", help="toggle log messages")
	parser.add_argument("-g", "--group_size", type=int, default=2, help="how many pixels each image tkaes in the mosaic")
	parser.add_argument("-t", "--tile_size", type=int, default=32, help="quality of each individual image in the mosaic")
	args = parser.parse_args()

	# For testing :-)
	# image_path = "hotdog.jpg"

	im = Image.open(args.file)
	makeMosaic(im, args.keyword, args.tile_size, args.group_size, args.file, args.verbose)

if __name__ == "__main__":
	main()

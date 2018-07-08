#!/usr/bin/env python
from PIL import Image


def getRGBArray(im):
	width, height = im.size
	rgb_arr = [[(0,0,0) for i in range(width)] for i in range(height)]

	for i in range(height):
		for j in range(width):
			# Reverse width/height for getpixel
			rgb_arr[i][j] = im.convert('RGB').getpixel((j,i))
	return rgb_arr

def getAverageColour(im):
	rgb_array = getRGBArray(im)
	width, height = im.size
	avg_r = 0
	avg_g = 0
	avg_b = 0
	for i in range(height):
		for j in range(width):
			r, g, b = rgb_array[i][j]
			avg_r += r
			avg_g += g
			avg_b += b

	num_pixels = width * height
	return (avg_r / num_pixels, avg_g / num_pixels, avg_b / num_pixels)

def getMostAppropriateImage(rgb, picture_map):
	min_distance = float("inf")
	min_image = None
	for (colour, image) in picture_map:
		dist = (colour[0] - rgb[0])**2 + (colour[1] - rgb[1])**2 + (colour[2] - rgb[2])**2
		if (dist < min_distance):
			min_distance = dist
			min_image = image

	return min_image

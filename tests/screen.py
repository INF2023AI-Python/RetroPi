import pygame
from PIL import Image
from PIL import ImageDraw
from rgbmatrix import RGBMatrix, RGBMatrixOptions

image = Image.new("RGB", (32, 32))
draw = ImageDraw.Draw(image)

options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
matrix = RGBMatrix(options=options)

for i in range(32 * 32):
    draw.point((i % 32, i % 32), fill=(255, 255, 255))
    matrix.SetImage(image, 0, 0)

import pygame
from PIL import Image
from PIL import ImageDraw
try:
    from RGBMatrixEmulator import RGBMatrix, RGBMatrixOptions
except ImportError:
    from rgbmatrix import RGBMatrix, RGBMatrixOptions

options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'

matrix = RGBMatrix(options=options)

image = Image.new("RGB", (32, 32))
draw = ImageDraw.Draw(image)

running = True
while running:
    draw.rectangle((0,0,32,32),fill=(222,0,0,0))
    matrix.SetImage(image, 0, 0)
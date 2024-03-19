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


    draw.rectangle((1,1,10,10),fill=(234,182,118))
    draw.rectangle((11,1,20,10),fill=(255,0,0,0))
    draw.rectangle((21,1,30,10),fill=(255,0,0,0))

    draw.rectangle((1,11,10,20),fill=(255,0,0,0))
    draw.rectangle((11,11,20,20),fill=(234,182,118))
    draw.rectangle((21,11,30,20),fill=(255,0,0,0))

    draw.rectangle((1,21,10,30),fill=(255,0,0,0))
    draw.rectangle((11,21,20,30),fill=(234,182,118))
    draw.rectangle((21,21,30,30),fill=(255,0,0,0))

    draw.rectangle((2,2,9,9),fill=(0,0,0,0))
    draw.rectangle((12,2,19,9),fill=(0,0,0,0))
    draw.rectangle((22,2,29,9),fill=(0,0,0,0))

    draw.rectangle((2,12,9,19),fill=(0,0,0,0))
    draw.rectangle((12,12,19,19),fill=(0,0,0,0))
    draw.rectangle((22,12,29,19),fill=(0,0,0,0))

    draw.rectangle((2,22,9,29),fill=(0,0,0,0))
    draw.rectangle((12,22,19,29),fill=(0,0,0,0))
    draw.rectangle((22,22,29,29),fill=(0,0,0,0))

    matrix.SetImage(image, 0, 0)
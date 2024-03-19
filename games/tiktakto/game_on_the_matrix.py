import pygame
from PIL import Image
from PIL import ImageDraw
try:
    from RGBMatrixEmulator import RGBMatrix, RGBMatrixOptions
except ImportError:
    from rgbmatrix import RGBMatrix, RGBMatrixOptions

player_circle = set([])
player_x = set([])

#Colors
RED=(255, 0, 0)
BLUE=(255, 0, 43)
WHITE=(255, 255, 255)
BLACK=(0, 0, 0)

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


    #DRAWS X
    draw.line((i[0] + 1, i[1] + 1, i[0] + 9,i[1] + 9),fill=RED)
    draw.line((i[0] + 1,i[1] + 9,i[0] + 9,i[1] + 1),fill=RED)

    #DRAWS O
    draw.ellipse((b[0] + 1, b[1] + 1, b[0] + 9,b[1] + 9),fill=BLUE)


    #DRAWS GRID
    draw.rectangle((0,0,32,32),fill=WHITE)

    draw.rectangle((2,2,9,9),fill=BLACK)
    draw.rectangle((12,2,19,9),fill=BLACK)
    draw.rectangle((22,2,29,9),fill=BLACK)

    draw.rectangle((2,12,9,19),fill=BLACK)
    draw.rectangle((12,12,19,19),fill=BLACK)
    draw.rectangle((22,12,29,19),fill=BLACK)

    draw.rectangle((2,22,9,29),fill=BLACK)
    draw.rectangle((12,22,19,29),fill=BLACK)
    draw.rectangle((22,22,29,29),fill=BLACK)

    matrix.SetImage(image, 0, 0)
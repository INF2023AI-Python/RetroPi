import pygame
from PIL import Image
from PIL import ImageDraw
from rgbmatrix import RGBMatrix, RGBMatrixOptions

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

print("Found:", joystick.get_name())

import pygame
from PIL import Image
from PIL import ImageDraw
try:
    import RGBMatrixEmulator
except ImportError:
    from rgbmatrix import RGBMatrix, RGBMatrixOptions

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

running = True
while running:
    print("Found:", joystick.get_name())
    for i in range(joystick.get_numaxes()-1):
        print("axis: ",joystick.get_axis(i))
    print(joystick.get_id())
    print(joystick.get_guid())


import board
import neopixel
import time

class cube:
    def __init__(self, x, y, z):
        self.dim_x = x
        self.dim_y = y
        self.dim_z = z
        self.pixels = neopixel.NeoPixel(board.D18, x*y*z, pixel_order=(0, 1, 2), auto_write=False)
    def pixel(self, x, y, z, color):
        self.pixels[x*25+y*5+z] = color
    def show(self):
        self.pixels.show()
    def fill(self, color):
        self.pixels.fill(color)
import board
import neopixel
import time

def validate(color):
        if color[0] < 0 :
            color[0] = 0
        if color[1] < 0 :
            color[1] = 0
        if color[2] < 0 :
            color[2] = 0
        if color[0] > 255:
            color[0] = 255
        if color[1] > 255:
            color[1] = 255
        if color[2] > 255:
            color[2] = 255
        return color

class cube:
    def __init__(self, x, y, z):
        self.dim_x = x
        self.dim_y = y
        self.dim_z = z
        self.pixels = neopixel.NeoPixel(board.D18, x*y*z, pixel_order=(0, 1, 2), auto_write=False)
    def pixel(self, x, y, z, color):
        self.pixels[x*25+y*5+z] = validate(color)
    def get_pixel(self, x, y, z):
        return self.pixels[x*25+y*5+z]
    def show(self):
        self.pixels.show()
    def fill(self, color):
        self.pixels.fill(validate(color))

    

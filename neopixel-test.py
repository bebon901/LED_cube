import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 30)
pixels.fill((255, 0, 0))
pixels.show()

time.sleep(5)
pixels.fill((0, 0, 0))
pixels.show()
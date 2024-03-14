import led_cube
import colorsys
import time
import math

cube = led_cube.cube(5, 5, 5)

while True:
    for rot in range(100000):
        cube.fill((0, 0, 0))
        for x in range(5):
            for y in range(5):
                cube.pixel(x, y, int(2.5*math.sin(x + rot/15) + 2.5), (255, 0, 255))
        time.sleep(0.01)
        cube.show()
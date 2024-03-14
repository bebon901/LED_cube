import led_cube
import colorsys
import time

cube = led_cube.cube(5, 5, 5)
while True:
    for rot in range(0, 100, 10):
        for x in range(5):
            cube.fill((0, 0, 0))
            for y in range(5):
                for z in range(5):
                    cube.pixel(x, y, z, tuple(i * 255 for i in colorsys.hsv_to_rgb(z*5/255+rot/100, 1, 1)))
            time.sleep(0.15)
            cube.show()
        for x in range(3):
            cube.fill((0, 0, 0))
            for y in range(5):
                for z in range(5):
                    cube.pixel(3-x, y, z, tuple(i * 255 for i in colorsys.hsv_to_rgb(z*5/255+rot/100, 1, 1)))
            time.sleep(0.15)
            cube.show()
import led_cube
import colorsys
import time

cube = led_cube.cube(5, 5, 5)

while True:
    for rot in range(100):
        for x in range(5):
            for y in range(5):
                for z in range(5):
                    cube.pixel(x, y, z, tuple(i * 255 for i in colorsys.hsv_to_rgb(z/30+rot/100 + y/30+x/30, 1, 1)))
        time.sleep(0.15)
        cube.show()

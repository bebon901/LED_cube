import led_cube
import colorsys
import time

cube = led_cube.cube(5, 5, 5)
while True:
    for dist in range(0, 100):
        cube.fill((0, 0, 0))
        for x in range(5):
            for y in range(5):
                for z in range(5):
                    if ((dist/10)**2 - 9) <= (x**2 + y**2 + z**2) and (x**2 + y**2 + z**2) <= (dist/10)**2:
                        cube.pixel(x, y, z, tuple(i * 255 for i in colorsys.hsv_to_rgb(dist/250, 1, 1)))
        time.sleep(0.025)
        cube.show()
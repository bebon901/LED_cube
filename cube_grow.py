import led_cube
import colorsys
import time

cube = led_cube.cube(5, 5, 5)
while True:
    for size in range(5):
        for x in range(5):
            for y in range(5):
                for z in range(5):
                    if (x <= size and y <= size and z <= size):
                        cube.pixel(x, y, z, (0, 255, 255))
        time.sleep(0.2)
        cube.show()
    cube.fill((0, 0, 0))
    for size2 in range(5):
        size = 4 - size2
        cube.fill((0, 0, 0))
        for x in range(5):
            for y in range(5):
                for z in range(5):
                    if (x <= size and y <= size and z <= size):
                        cube.pixel(x, y, z, (0, 255, 255))
        time.sleep(0.2)
        cube.show()
    
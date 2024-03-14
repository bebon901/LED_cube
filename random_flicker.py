import led_cube
import colorsys
import time
import random
import numpy as np
cube = led_cube.cube(5, 5, 5)
timer = 0
while True:
    if timer % 5 == 4:
        cube.pixel(random.randint(0, 4), random.randint(0, 4), random.randint(0, 4), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        
    print(cube.get_pixel(0, 0,0) - np.array([5, 5, 5]))
    for x in range(5):
        for y in range(5):
            for z in range(5):
                cube.pixel(x, y, z, np.array(cube.get_pixel(x, y, z)) - np.array([5, 5, 5]))
    cube.show()
    time.sleep(0.05)
    timer += 1

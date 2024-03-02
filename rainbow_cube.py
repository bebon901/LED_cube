import led_cube
import colorsys
import time

cube = led_cube.cube(5, 5, 5)
while True:
    for rot in range(100):
        for x in range(5):
            for y in range(5):
                for z in range(5):
                    cube.pixel(x, y, z, (colorsys.hsv_to_rgb(z*5/255+rot/100, 1, 1)[0]*255, colorsys.hsv_to_rgb(z*5/100+rot/255, 1, 1)[1]*255, colorsys.hsv_to_rgb(z*5/255+rot/100, 1, 1)[2]*255))
    time.sleep(0.0001)
    cube.show()
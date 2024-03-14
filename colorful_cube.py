import led_cube
import colorsys
import time

cube = led_cube.cube(5, 5, 5)
def loop(x, low, top):
    print(x)
    print(low <= x and x <= top)
    if low < x and x < top:
        return x
    else:
        return loop(x-top+low, low, top)
while True:
    for rot in range(100):
        for x in range(5):
            for y in range(5):
                for z in range(5):
                    cube.pixel(x, y, z, tuple(i * 255 for i in colorsys.hsv_to_rgb(z/10+rot/100 + y/10+x/10, 1, 1)))
        time.sleep(0.05)
        cube.show()
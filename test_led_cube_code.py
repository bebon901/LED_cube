import led_cube

cube = led_cube.cube(5, 5, 5)
cube.fill((255, 0, 255))
cube.pixel(0, 0, 0, (0, 255, 0))
cube.pixel(0, 1, 1, (0, 255, 0))
cube.pixel(0, 2, 2, (0, 255, 0))
cube.pixel(0, 3, 3, (0, 255, 0))
cube.pixel(0, 4, 4, (0, 255, 0))
cube.show()
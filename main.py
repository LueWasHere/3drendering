# Importing pygame module
import pygame
from pygame.locals import *
import math
from time import sleep
"""
with open('main.mdl', 'wb') as f:
    f.write(b'\01,\255[\255[\255|')
    f.close()"""

def rotate_around_origin(point: tuple, scotts_rotation: int=0) -> tuple: # the point will be pygame coords so we hve to convert it
    rotation_in_radians = scotts_rotation/63.6942675
    x_coord = (math.sin(rotation_in_radians)*point[0])+(math.cos(rotation_in_radians)*point[1])
    y_coord = math.sin(rotation_in_radians)*point[1]
    return (y_coord, x_coord)
print(rotate_around_origin((0, 1), 50))

# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))
size = (600, 600)

points = []
inc = True
for i in range(0, 400):
    points_t = rotate_around_origin((0, 300), i)
    points_t = (math.floor(points_t[0]+300), math.floor((points_t[1]*-1)+300), 0)
    points.append(points_t)
pointer = 0

while True: 
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    # Fill the scree with black color
    window.fill((0, 0, 0))

    pointer += 1
    if pointer > len(points)-1:
        pointer = 0

    #print(point)
    #window.set_at(points[pointer], (255, 255, 255, 0.0))
    pygame.draw.circle(window, (255-points[pointer][2], 255-points[pointer][2], 255-points[pointer][2], 0), (points[pointer][0], points[pointer][1]), 5)
    sleep(0.01)
    # Draws the surface object to the screen.
    pygame.display.update()
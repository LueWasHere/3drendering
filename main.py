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
#print(rotate_around_origin((0, 1), 50))

# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension.
size = (600, 600)
z_bound = size[0]
window = pygame.display.set_mode(size)

#points = []
world = [[(300, 300, -10, ), (300, 289, 0), (289, 289, 0), (289, 300, 0), (300, 300, 0)]]
#inc = True
"""for i in range(0, 400):
    points_t = rotate_around_origin((0, z_bound/2), i)
    points_t = (size[0]/2, math.floor(points_t[0]+size[1]/2), math.floor((points_t[1]*-1)+z_bound/2))
    points.append(points_t)"""
pointer = 0
inc = 0
dec = False
while True: 
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    # Fill the scree with black color
    window.fill((0, 0, 0))

    # the point closest to the origin does not change, the rest should scale to the z coord
    offsets = []
    distance = []
    dne_point_index = 0
    for object in world:
        for point in object:
            # calculate the distance from the origin
            distance.append(math.sqrt((point[0]-size[0]/2)**2+(point[1]-size[1]/2)**2))
        temp = min(distance)
        res = [i for i, j in enumerate(distance) if j == temp]
        res = res[0]
        new = []
        for i,point in enumerate(object):
            if point[2] != 0:
                z_offset = math.sqrt((point[1]-size[1]/2)**2+(point[2]-z_bound/2)**2) # just the distance of the z and y coords of a given point from the origin
                if i != res:
                    if point[0] != object[res][0] and point[1] != object[res][1]:
                        if point[0] > object[res][0] and point[1] > object[res][1]:
                            new.append((point[0]+z_offset, point[1]+z_offset))
                        elif point[0] > object[res][0] and point[1] < object[res][1]:
                            new.append((point[0]+z_offset, point[1]-z_offset))
                        else:
                            new.append((point[0]-z_offset, point[1]-z_offset))
                    elif point[0] != object[res][0] and point[1] == object[res][1]:
                        if point[0] > object[res][0]:
                            new.append((point[0]+z_offset, point[1]))
                        else:
                            new.append((point[0]-z_offset, point[1]))
                    elif point[0] == object[res][0] and point[1] != object[res][1]:
                        if point[1] > object[res][1]:
                            new.append((point[0], point[1]+z_offset))
                        else:
                            new.append((point[0], point[1]-z_offset))
                else:
                    new.append((point[0], point[1]))
            else:
                new.append((point[0], point[1]))
            # dont remove this
            object[-1] = object[0] # THIS
        offsets = []
        distance = []
        pygame.draw.polygon(window, (255, 255, 255), new, 1)


    """pointer += 1
    if pointer > len(points)-1:
        pointer = 0"""

    #print(point)
    #window.set_at(points[pointer], (255, 255, 255, 0.0))
    """points_c = ()
    for point_pair in points:
        if points[pointer][0] > points[pointer][1]:
            points_c = (points[pointer][0]+points[pointer][2], points[pointer][1])
        else:
            points_c = (points[pointer][0], points[pointer][1]+points[pointer][2])"""
    #pygame.draw.circle(window, (255, 255, 255, 0), points_c, points[pointer][2]/2)
    sleep(0.01)
    # Draws the surface object to the screen.
    pygame.display.update()
    #input() # wait for the enter key
import pygame,time,sys
from Box2D import *
import objects, draw

draw.init()
objects.init()

#    print body.position, body.angle
while 1:
    objects.Step()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
	if event.type == pygame.MOUSEBUTTONUP:
	       	objects.create_ball(draw.Inverse_Transform_Vertex(event.pos),
				10)
    
#time.sleep(0.1)

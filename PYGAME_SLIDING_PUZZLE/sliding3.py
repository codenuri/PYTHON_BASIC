import sys
import pygame
from pygame.locals import QUIT

pygame.init()

image = pygame.image.load('sliding.jpg')
rect  = image.get_rect()
surface = pygame.display.set_mode((rect.width,rect.height))

COUNT = 5
BW = rect.width / COUNT
BH = rect.height / COUNT

surface.fill((255,255,255))

no = 11
bx = no % COUNT
by = no // COUNT
surface.blit( image, (0, 0),
				     (bx * BW, by * BH, BW, BH))

pygame.display.update()

while True:
	e = pygame.event.wait()
	if e.type == QUIT:
		pygame.quit()
		sys.exit()

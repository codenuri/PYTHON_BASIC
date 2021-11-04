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

no = 0
for y in range(0, COUNT):
	for x in range(0, COUNT):	
		bx = no % COUNT
		by = no // COUNT
		surface.blit( image, (x * BW, y * BH), (bx * BW, by * BH, BW - 1, BH - 1))
		no += 1



pygame.display.update()





while True:
	e = pygame.event.wait()
	if e.type == QUIT:
		pygame.quit()
		sys.exit()

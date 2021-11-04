import sys
import pygame
from pygame.locals import QUIT

pygame.init()

image = pygame.image.load('sliding.jpg')
rect  = image.get_rect()
surface = pygame.display.set_mode((rect.width,rect.height))

COUNT = 5
EMPTY = COUNT * COUNT - 1
BW = rect.width / COUNT
BH = rect.height / COUNT

state = [[ 0, 1, 2, 3, 4],
         [ 5, 6, 7, 8, 9],
		 [10,11,12,13,14],
		 [15,16,17,18,19],
		 [20,21,22,23,24]]

surface.fill((255,255,255))

for y in range(0, COUNT):
	for x in range(0, COUNT):		
		no = state[y][x]
		if no != EMPTY:				
			bx = no % COUNT
			by = no // COUNT
			surface.blit( image, (x * BW, y * BH), (bx * BW, by * BH, BW - 1, BH - 1))

pygame.display.update()





while True:
	e = pygame.event.wait()
	if e.type == QUIT:
		pygame.quit()
		sys.exit()

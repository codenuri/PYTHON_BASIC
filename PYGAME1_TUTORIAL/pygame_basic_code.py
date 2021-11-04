import pygame
import sys
from pygame.locals import QUIT

pygame.init()

surface = pygame.display.set_mode( (300, 200) )

surface.fill((255, 255, 255))


pygame.display.update()

while True:
	e = pygame.event.wait()

	if e.type == QUIT:
		pygame.quit()
		sys.exit()
		

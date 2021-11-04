import pygame
import sys
import pygame.locals

pygame.init()

pygame.display.set_mode( (300, 200) )

while True:
	e = pygame.event.wait()
	if e.type == pygame.locals.QUIT:
		pygame.quit()
		sys.exit()
	

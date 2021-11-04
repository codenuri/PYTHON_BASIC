import pygame
import sys
import pygame.locals

pygame.init()

surface = pygame.display.set_mode( (300, 300) )

surface.fill( (255, 255, 255))

pygame.display.update()

while True:
	e = pygame.event.wait()
	if e.type == pygame.locals.QUIT:
		pygame.quit()
		sys.exit()
	

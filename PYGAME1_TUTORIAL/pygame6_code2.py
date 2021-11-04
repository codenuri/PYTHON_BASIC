import pygame
import sys
from pygame.locals import QUIT, MOUSEBUTTONDOWN, KEYDOWN, K_LEFT, K_RIGHT

pygame.init()

surface = pygame.display.set_mode( (300, 200) )

surface.fill((255, 255, 255))

pygame.display.update()

while True:
	e = pygame.event.wait()

	if e.type == QUIT:
		pygame.quit()
		sys.exit()

	elif e.type == MOUSEBUTTONDOWN:
		if e.button == 1:
			print('LBUTTON')
		elif e.button == 3:
			print('RBUTTON')

	elif e.type == KEYDOWN:
		if e.key == K_LEFT:
			print('LEFT ARROW')
		elif e.key == K_RIGHT:
			print('RIGHT ARROW')
		



			

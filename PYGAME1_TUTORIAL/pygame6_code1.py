import pygame
import sys
import pygame.locals

pygame.init()

surface = pygame.display.set_mode( (300, 200) )

surface.fill((255, 255, 255))

pygame.display.update()

while True:
	e = pygame.event.wait()

	if e.type == pygame.locals.QUIT:
		pygame.quit()
		sys.exit()

	elif e.type == pygame.locals.MOUSEBUTTONDOWN:
		if e.button == 1:
			print('LBUTTON')
		elif e.button == 3:
			print('RBUTTON')

	elif e.type == pygame.locals.KEYDOWN:
		if e.key == pygame.locals.K_LEFT:
			print('LEFT ARROW')
		elif e.key == pygame.locals.K_RIGHT:
			print('RIGHT ARROW')
		



			

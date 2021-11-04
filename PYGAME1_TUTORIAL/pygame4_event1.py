import pygame

pygame.init()

pygame.display.set_mode( (300, 200) )

while True:
	e = pygame.event.wait()
	print(e)

pygame.quit()

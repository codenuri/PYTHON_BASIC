import pygame
import sys
import pygame.locals

pygame.init()

surface = pygame.display.set_mode( (300, 300) )


surface.fill( (255, 255, 255))

pygame.draw.line(surface, (255, 0, 0), (0, 0), (100,100), 15) # 두께 15
pygame.draw.line(surface, (0, 0, 255), (100, 100), (300,100)) # 두께 인자 생략시 1
pygame.draw.rect(surface, (0, 255, 0), (150, 10, 100, 30), 3)
pygame.draw.circle(surface, (255, 0, 255), (150, 50), 50, 10)

pygame.display.update()


while True:
	e = pygame.event.wait()
	if e.type == pygame.locals.QUIT:
		pygame.quit()
		sys.exit()
	

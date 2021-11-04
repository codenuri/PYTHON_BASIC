import sys
import pygame
from pygame.constants import MOUSEBUTTONDOWN
from pygame.locals import QUIT

pygame.init()

image = pygame.image.load("sliding.jpg")
rect = image.get_rect()

COUNT = 5
EMPTY = COUNT * COUNT - 1  
bw = rect.width / COUNT
bh = rect.height / COUNT

# 게임판 초기화
board = []

for y in range(0, COUNT):
	temp = []
	for x in range(0, COUNT):
		temp.append(y * COUNT + x)
	board.append(temp)

SURFACE  = pygame.display.set_mode((rect.width, rect.height))
pygame.display.set_caption('Slidig Puzzle Game')

FPSCLOCK = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEBUTTONDOWN:
			if event.button == 1:
				x, y = pygame.mouse.get_pos()
				bx = int(x // bw)
				by = int(y // bh)
				if by > 0 and board[by-1][bx] == EMPTY:
					board[by][bx], board[by-1][bx] = board[by-1][bx], board[by][bx]
				elif by < COUNT-1 and board[by+1][bx] == EMPTY:
					board[by][bx], board[by+1][bx] = board[by+1][bx], board[by][bx]
				elif bx > 0 and board[by][bx-1] == EMPTY:
					board[by][bx], board[by][bx-1] = board[by][bx-1], board[by][bx]
				elif bx < COUNT-1 and board[by][bx+1] == EMPTY:
					board[by][bx], board[by][bx+1] = board[by][bx+1], board[by][bx]

	SURFACE.fill((255, 255, 255))
	
	for y in range(0, COUNT):
		for x in range(0, COUNT):
			block_no = board[y][x]
			
			if ( block_no != EMPTY ):
				bx = block_no % COUNT
				by = block_no // COUNT
				SURFACE.blit(image, [x*bw, y*bh], [bx * bw, by * bh, bw-1, bh-1] )

	pygame.display.update()
	FPSCLOCK.tick(30)



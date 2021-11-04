import sys
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN

def draw_game():
	surface.fill((255,255,255))

	for y in range(0, COUNT):
		for x in range(0, COUNT):		
			no = state[y][x]
			if no != EMPTY:				
				bx = no % COUNT
				by = no // COUNT
				surface.blit( image, (x * BW, y * BH), (bx * BW, by * BH, BW - 1, BH - 1))

	pygame.display.update()


pygame.init()

# 1. 그림 로드, 윈도우 생성
image = pygame.image.load('sliding.jpg')
rect  = image.get_rect()
surface = pygame.display.set_mode((rect.width,rect.height))

# 2. 변수, 리스트 초기화
COUNT = 5
EMPTY = COUNT * COUNT - 1
BW = rect.width / COUNT
BH = rect.height / COUNT

state = []

for y in range(0, COUNT):
	s = []
	for x in range(0, COUNT):
		s.append(x + y * COUNT)
	state.append(s)

# 3. 게임 화면(블럭) 출력
draw_game()

# 4. 이벤트 처리
while True:
	e = pygame.event.wait()
	if e.type == QUIT:
		pygame.quit()
		sys.exit()

	elif e.type == MOUSEBUTTONDOWN:
		if e.button == 1: # LBUTTON
			x, y = pygame.mouse.get_pos() #(x, y)
			bx = int(x // BW)
			by = int(y // BH)
			
			if by > 0 and state[by-1][bx] == EMPTY:	# 클릭한 곳의 위가 비었는가 ?
				state[by][bx], state[by-1][bx] = state[by-1][bx], state[by][bx]
			elif by < COUNT-1 and state[by+1][bx] == EMPTY:
				state[by][bx], state[by+1][bx] = state[by+1][bx], state[by][bx]
			elif bx > 0 and state[by][bx-1] == EMPTY:
				state[by][bx], state[by][bx-1] = state[by][bx-1], state[by][bx]
			elif bx < COUNT-1 and state[by][bx+1] == EMPTY:
				state[by][bx], state[by][bx+1] = state[by][bx+1], state[by][bx]
			else:
				continue

			# state 리스트가 변경되었으므로 블럭을 다시 그린다.
			draw_game()



import random

cv = [-1, -1, -1]

cv[0] = random.randrange(0, 10)

for i in range(1, 3):
	while True:
		n = random.randrange(0, 10)
		if n not in cv:
			cv[i] = n
			break

while True:
	iv = [0, 0, 0]

	for i in range(0,3):
		iv[i] = int(input(f'{i+1} 번째 숫자를 입력하세요 >> '))

	ball = 0
	strike = 0

	for i in range(0, 3):
		if iv[i] == cv[i]:
			strike += 1
		elif iv[i] in cv:
			ball += 1

	print(f'{strike} strike, {ball} ball')

	if strike == 3:
		print('성공')
		break

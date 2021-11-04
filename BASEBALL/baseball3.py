# 중복되지 않은 정수형 난수 3개 구하기.
import random

cv = [-1, -1, -1]

cv[0] = random.randrange(0, 10)

while True:
	cv[1] = random.randrange(0, 10)
	if cv[1] != cv[0]:
		break

while True:
	cv[2] = random.randrange(0, 10)
	if cv[2] != cv[1] and cv[2] != cv[0]:
		break

print(cv[0], cv[1], cv[2])

# 중복되지 않은 정수형 난수 3개 구하기.
import random

#     3, -1, -1
cv = [-1, -1, -1]

cv[0] = random.randrange(0, 10)

for i in range(1, 3):
	while True:
		n = random.randrange(0, 10)
		if n not in cv:
			cv[i] = n
			break

print(cv[0], cv[1], cv[2])

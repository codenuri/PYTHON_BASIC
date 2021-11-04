# 정수형 난수 3개 구하기

import random

#r1 = random.random()       # 실수, 0 ~ 1 (0.345)
#r2 = random.uniform(0, 10) # 실수, 0 ~ 10
#r3 = random.randrange(0, 10) # 정수, 0 ~ 10

#print(r1, r2, r3)

cv = [-1, -1, -1]

cv[0] = random.randrange(0, 10)
cv[1] = random.randrange(0, 10)
cv[2] = random.randrange(0, 10)

print(cv[0], cv[1], cv[2])

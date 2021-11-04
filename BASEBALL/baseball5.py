# strike, ball 판정

cv = [1,3,5]  # 컴퓨터가 생각한 숫자
iv = [1,5,9]  # 사용자가 입력한 숫자

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




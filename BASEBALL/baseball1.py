# 3개의 정수 입력 받기

#a = int(input())
#b = int(input())
#c = int(input())

iv = [0, 0, 0]

for i in range(0,3):
	iv[i] = int(input(f'{i+1} 번째 숫자를 입력하세요 >> '))

print(iv[0], iv[1], iv[2])
print('Mo Tu We Th Fr Sa Su')

for i in range(1, 32):
	print(f'{i:2} ', end='')

	if i % 7 == 0:
		print()
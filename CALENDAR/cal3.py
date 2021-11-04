days = ( 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

year = 2022
month = 11

dayofweek = 4

print('Mo Tu We Th Fr Sa Su')

print(' ' * 3 * dayofweek, end = '')

for i in range(1, days[month - 1] + 1):
	print(f'{i:2} ', end='')
	if ( i + dayofweek ) % 7 == 0:
		print()

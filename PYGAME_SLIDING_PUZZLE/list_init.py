COUNT = 5

state = [[ 0, 1, 2, 3, 4],
         [ 5, 6, 7, 8, 9],
		 [10,11,12,13,14],
		 [15,16,17,18,19],
		 [20,21,22,23,24]]

state = []

for y in range(0, COUNT):
	s = []
	for x in range(0, COUNT):
		s.append(x + y * COUNT)
	state.append(s)


print(state)




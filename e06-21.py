def checker(input):
	grid = 9
	subgrid_size = 3
	#check grid rows (n^2)
	for row in input:
		dic = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
		for item in row:
			if item != 0:
				current_value = dic[item]
				dic[item] = current_value + 1
		for key, value in dic.iteritems():
			if value > 1:
				return False

	#check grid columns (n^2)
	for column in range(0,grid-1):
		dic = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
		for i in range(0,grid-1):
			if input[i][column] != 0:
				current_value = dic[input[i][column]]
				dic[input[i][column]] = current_value + 1
		for key, value in dic.iteritems():
			if value > 1:
				return False

	#check inside subgrids (n^2)
	dic1 = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
	dic2 = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
	dic3 = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
	for i in range(0,2):
		for j in range(0,8):
			if input[i][j] != 0:
				if j < 2:
					current_value = dic1[input[i][j]]
					dic1[input[i][j]] = current_value + 1					
				elif j < 5:
					current_value = dic2[input[i][j]]
					dic2[input[i][j]] = current_value + 1					
				else:
					current_value = dic3[input[i][j]]
					dic3[input[i][j]] = current_value + 1 
	
	for key, value in dic.iteritems():
		if value > 1:
			return False


	dic1 = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
	dic2 = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
	dic3 = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
	for i in range(3,5):
		for j in range(0,8):
			if input[i][j] != 0:
				if j < 2:
					current_value = dic1[input[i][j]]
					dic1[input[i][j]] = current_value + 1					
				elif j < 5:
					current_value = dic2[input[i][j]]
					dic2[input[i][j]] = current_value + 1					
				else:
					current_value = dic3[input[i][j]]
					dic3[input[i][j]] = current_value + 1 
	
	for key, value in dic.iteritems():
		if value > 1:
			return False	

	dic1 = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
	dic2 = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
	dic3 = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
	for i in range(6,8):
		for j in range(0,8):
			if input[i][j] != 0:
				if j < 2:
					current_value = dic1[input[i][j]]
					dic1[input[i][j]] = current_value + 1					
				elif j < 5:
					current_value = dic2[input[i][j]]
					dic2[input[i][j]] = current_value + 1					
				else:
					current_value = dic3[input[i][j]]
					dic3[input[i][j]] = current_value + 1 
	
	for key, value in dic.iteritems():
		if value > 1:
			return False	

	return True

input = [[5,3,0, 0,7,0, 0,0,0], 
		 [6,0,0, 1,9,5, 0,0,0], 
		 [0,9,8, 0,0,0, 0,6,0],

		 [8,0,0, 0,6,0, 0,0,3], 
		 [4,0,0, 8,0,3, 0,0,1], 
		 [7,0,0, 0,2,0, 0,0,6], 
		 
		 [0,6,0, 0,0,0, 2,8,0], 
		 [0,0,0, 4,1,9, 0,0,5], 
		 [0,0,0, 0,8,0, 0,7,9]]
		 
print checker(input)
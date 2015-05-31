def all_n_queens(n, out):
	col = len(out)
	if col == n:
		print out
	else:
		for row in range(0,n):
			out.append((row,col))
			if is_valid(out):
				all_n_queens(n, out)
			out.pop()

def n_queens(n, out):
	col = len(out)
	if col == n:
		return True
	else:
		for row in range(0,n):
			out.append((row,col))
			if is_valid(out) and n_queens(n,out):
				return True
			else:
				out.pop()
		return False


def is_valid(out):
	for i in range(0,len(out)):
		for j in range(i+1,len(out)):
			if is_same_c(i,j,out) or is_same_r(i,j,out) or is_same_d(i,j,out):
				return False
	return True

def is_same_c(i,j,out):
	return out[i][1] == out[j][1]

def is_same_r(i,j,out):
	return out[i][0] == out[j][0]

def is_same_d(i,j,out):
	return is_left_u(i,j,out) or is_left_d(i,j,out) or is_right_u(i,j,out) or is_right_d(i,j,out)

def is_left_u(i,j,out):
	return out[i][0] == out[j][0]-1 and out[i][1] == out[j][1]-1

def is_left_d(i,j,out):
	return out[i][0] == out[j][0]+1 and out[i][1] == out[j][1]-1

def is_right_u(i,j,out):
	return out[i][0] == out[j][0]-1 and out[i][1] == out[j][1]+1

def is_right_d(i,j,out):
	return out[i][0] == out[j][0]+1 and out[i][1] == out[j][1]+1

s = []
all_n_queens(4, s)
print s
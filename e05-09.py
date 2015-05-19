def unspreadsheeter(id):
	mult = 1
	result = 0
	for digit in id[::-1]:
		if digit == 'A':
			result = result + mult * 1
		elif digit == 'B':
			result = result + mult * 2
		else:
			result = result + mult * 3
		mult = mult * 3

	return result				




print unspreadsheeter("A") #1
print unspreadsheeter("B") #2
print unspreadsheeter("AA") #4
print unspreadsheeter("BA") #7
print unspreadsheeter("BC") #89
#1 2 3  4  5  6  7  8  9
#A-B-C-AA-AB-AC-BA-BB-BC
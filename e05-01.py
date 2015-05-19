def parity_checker(dec_n):
	ones_counter = 0
	for bit in bin(dec_n):
		if bit == '1':
			ones_counter = ones_counter + 1
	if ones_counter % 2 == 0:
		return True
	else:
		return False



number10 = 10 #true
number11 = 11 #false
print parity_checker(number10)
print parity_checker(number11)
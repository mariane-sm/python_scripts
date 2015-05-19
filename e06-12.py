def primes(n):
	primes = []
	for number in range(2,n):
		if number % 2 != 0:
			is_prime = True
			for divisor in range(2, ((number/2) + 1)):
				if number % divisor == 0:
					is_prime = False
			if is_prime == True:
				primes.append(number)

	return primes

#2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43
print primes(46)
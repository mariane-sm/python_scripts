import copy

def calc(n, out, solutions):
	if sum(out) == n:
		out.sort()
		solutions.add(tuple(out))
	else:
		for number in [2,3,7]:
			x = copy.deepcopy(out)
			x.append(number)
			if is_valid(x, n):
				calc(n, x, solutions)


def is_valid(out, n):
	return sum(out) <= n

z = set()
calc(12, [], z)
print z;







import copy
def subsets(a, out):
	if len(a) > 0:
		for i in a:
			c = copy.deepcopy(a)
			c.remove(i)
			if c not in out:
				out.append(c)
			subsets(c, out)

def powerset(a, out=[]):
	subsets(a, out)
	out.append(a)
	return out

print powerset([1, 2, 3])


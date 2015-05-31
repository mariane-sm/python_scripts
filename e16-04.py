import copy
from itertools import chain

def ep(a):
	if len(a) > 1:
		output = []
		for i in a:
			c = copy.deepcopy(a)
			c.remove(i)
			for j in ep(c):
				output.append([i] + [j])
			#output.append([i] + ep(c))
		return output
	else:
		return a

def enumerations(a):
	items = ep(a)
	output = []
	for i in items:
		print flat(i)
		output.append(i)
	return output

def flat(a):
	out = []
	while len(a) > 0:
		item = a.pop(0)
		if type(item) is list:
			for i in item:
				a.append(i)
		else:
			out.append(item)
	return out

enumerations([1,2,3])

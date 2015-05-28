class Peg():
	def __init__(self,values,name):
		self.v = values
		self.name = name

p1 = Peg([3,2,1,0], "pegA") #disco 3 eh o de maior raio
p2 = Peg([], "pegB")
p3 = Peg([], "pegC")

def hanoi(n, src, dst, tmp):
	if (n > 0):
		hanoi(n-1, src, tmp, dst)
		src.v.remove(n)
		dst.v.append(n)
		print "move disc %d from %s to %s" %(n, src.name, dst.name)
		hanoi(n-1, tmp, dst, src)
	else:
		print "move disc %d from %s to %s" %(n, src.name, dst.name)
		src.v.remove(n)
		dst.v.append(n)


print p1.v
print p2.v
print p3.v
hanoi(3, p1, p3, p2)
print p1.v
print p2.v
print p3.v
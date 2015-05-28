class Peg:
	def __init__(self,values,name):
		self.v = values
		self.name = name

pegA = Peg([3,2,1,0], "pegA") #disco 3 eh o de maior raio
pegB = Peg([], "pegB")
pegC = Peg([], "pegC")

def hanoi(n, src, dst, tmp):
	if (n > 0):
		hanoi(n-1, src, tmp, dst) # move to middle all (n-1)
		move(n, src, dst)
		print "move disc %d from %s to %s" %(n, src.name, dst.name)
		hanoi(n-1, tmp, dst, src)
	else: # n == 0
		print "move disc %d from %s to %s" %(n, src.name, dst.name)
		move(n, src, dst)

def move(n, src, dst):
	src.v.remove(n)
	dst.v.append(n)

print pegA.v
print pegB.v
print pegC.v
hanoi(3, pegA, pegC, pegB)
print pegA.v
print pegB.v
print pegC.v
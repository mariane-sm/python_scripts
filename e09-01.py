class stack():
	items = []
	max = None

	def pop(self):
		if len(self.items) == 0:
			return None
		else:
			item = self.items.pop()

			if item == self.max:
				new_max = None
				for i in self.items:
					if new_max is None:
						new_max = i
					elif i > new_max:
						new_max = i

			return item
	
	def push(self, data):
		if self.max is None:
			self.max = data
		elif self.max < data:
			self.max = data
		self.items.append(data)

	def maximum(self):
		return self.max

#		max = -9999
#		my_items = []
#		while len(self.items) != 0:
#			x = self.pop()
#			my_items.append(x)
#			if x > max:
#				max = x
#		my_items.reverse()
#		for item in my_items:
#			self.push(item)
#		return max

#		max = -9999
#		for item in self.items:
#			if item > max:
#				max = item
#		return max

s = stack()
s.push(1)
s.push(2)
s.push(3)

print s.maximum()

print s.pop()
print s.pop()
print s.pop()

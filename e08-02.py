class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	head = None

	def show(self):
		output = []
		current_node = self.head
		while current_node is not None:
			output.append(current_node.data)
			current_node = current_node.next
		print output

	def append(self, data):
		node = Node(data)
		if self.head is None:
			self.head = node
		else:
			ptr = self.head
			while ptr.next is not None:
				ptr = ptr.next
			ptr.next = node	

	def reverse(self):
		paux = None
		n1 = self.head
		n2 = self.head.next
		while n2 is not None:
			n1.next = paux
			paux = n1
			n1 = n2
			n2 = n2.next
		n1.next = paux
		self.head = n1



s = LinkedList()
s.append(1)
s.append(2)
s.append(3)
s.append(4)
s.append(5)
s.show()
s.reverse()
s.show()

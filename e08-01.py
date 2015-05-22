class Node:
	def __init__(self,data):
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
			current_node = self.head
			while current_node.next is not None:
				current_node = current_node.next
			current_node.next = node

def merge(list1, list2):
	head = None
	aux1 = list1.head
	aux2 = list2.head
	paux = None

	while aux1 is not None or aux2 is not None:
		aux1data = 99999
		if aux1 is not None:
			aux1data = aux1.data
		aux2data = 99999
		if aux2 is not None:
			aux2data = aux2.data

		if aux1data < aux2data:
			if head is None:
				head = aux1
			else:
				if paux is not None:
					paux.next = aux1
				paux = aux1
				aux1 = aux1.next

		else:
			if head is None:
				head = aux2
			else:
				if paux is not None:
					paux.next = aux2
				paux = aux2
				aux2 = aux2.next

	output = []
	current_node = head
	while current_node is not None:
		output.append(current_node.data)
		current_node = current_node.next
	print output


s1 = LinkedList()
s1.append(2)
s1.append(5)
s1.append(9)
s1.append(81)
s1.show()

s2 = LinkedList()
s2.append(3)
s2.append(4)
s2.append(10)
s2.show()

merge(s1, s2)
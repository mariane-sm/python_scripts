class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	head = None

	def show(self):
		output = []
		current_ptr = self.head
		while current_ptr is not None:
			output.append(current_ptr.data)
			current_ptr = current_ptr.next
		print output

	def append(self, data):
		node = Node(data)
		if self.head is None:
			self.head = node
		else:
			current_ptr = self.head
			while current_ptr.next is not None:
				current_ptr = current_ptr.next
			current_ptr.next = node

    # returns None if there is no cycle
    # returns reference to start of cycle if there is one
	def cycle_finder(self):
		traversed_ptrs = set()
		current_ptr = self.head
		while current_ptr is not None:
			if current_ptr in traversed_ptrs:
				return current_ptr
			traversed_ptrs.add(current_ptr)
			current_ptr = current_ptr.next

		return None


list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
list1.append(5)
print list1.cycle_finder()

list2 = LinkedList()
list2.append(1)
list2.append(2)
list2.append(3)
list2.append(4)

output = []
ptr4 = list2.head
output.append(ptr4.data)
ptr4 = ptr4.next
output.append(ptr4.data)
ptr4 = ptr4.next
output.append(ptr4.data)
ptr4 = ptr4.next
output.append(ptr4.data)

ptr2 = list2.head
ptr2 = ptr2.next

ptr4.next = ptr2
output.append(ptr4.next.data)
print output

print list2.cycle_finder().data
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
	def __str__(self):
		return str(self.data)

def add_left(root, data):
	root.left = Node(data)
	return root.left

def add_right(root, data):
	root.right = Node(data)
	return root.right

#depth-first-traversing
#root left right
def traverse_pre_order(root, out):
	if root is not None:
		out.append(root.data)
		traverse_pre_order(root.left, out)
		traverse_pre_order(root.right, out)

#depth-first-traversing
#left root right
def traverse_in_order(root, out):
	if root is not None:
		traverse_in_order(root.left, out)
		out.append(root.data)
		traverse_in_order(root.right, out)

#depth-first-traversing
#left right root
def traverse_post_order(root, out):
	if root is not None:
		traverse_post_order(root.left, out)
		traverse_post_order(root.right, out)
		out.append(root.data)

#breadth-first
def traverse_breadth_first_order(siblings, out):
	new_siblings = []
	for node in siblings:
		out.append(node.data)
		if node.left is not None:
			new_siblings.append(node.left)
		if node.right is not None:
			new_siblings.append(node.right)
	if len(new_siblings) > 0:
		out.append("--")
		traverse_breadth_first_order(new_siblings, out)

bt = Node(1)
a1 = add_left(bt, 2)
a2 = add_right(bt, 3)
add_left(a1, 4)
a1 = add_right(a1, 5)
add_right(a1, 11)
add_right(a2, 7)
a1 = add_left(a2, 6)
add_left(a1, 12)
out = []
traverse_pre_order(bt, out)
print out
out = []
traverse_in_order(bt, out)
print out
out = []
traverse_post_order(bt, out)
print out
out = []
traverse_breadth_first_order([bt], out)
print out

         #1
    #2           #3
 #4  #5       #6    #7  
       #11  #12
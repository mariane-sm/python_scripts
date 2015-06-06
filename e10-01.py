#test if a binary tree is balanced
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

#breadth-first
def find_height(siblings, height=1):	
	new_siblings = []
	for node in siblings:
		if node.left is not None:
			new_siblings.append(node.left)
		if node.right is not None:
			new_siblings.append(node.right)
	if len(new_siblings) > 0:
		height = height + 1
		return find_height(new_siblings, height)
	else:
		return height

#depth-first-traversing
#root left right
def get_all_nodes(root, out):
	if root is not None:
		out.append(root)
		get_all_nodes(root.left, out)
		get_all_nodes(root.right, out)

#balanced tree: if for every node, the height diference for its left and right subtree
#is at most one
def is_balanced(root):
	nodes = []
	get_all_nodes(root, nodes)
	for node in nodes:
		if node.left is not None:
			left_height = find_height([node.left])
		else:
			left_height = 0
		if node.right is not None:
			right_height = find_height([node.right])
		else:
			right_height = 0
		if (abs(left_height - right_height) > 1):
			return False
	return True

bt = Node(1)
a1 = add_left(bt, 2)
a2 = add_right(bt, 3)
add_left(a1, 4)
a1 = add_right(a1, 5)
a1 = add_right(a1, 11)
add_right(a1, 20)
add_right(a2, 7)
a1 = add_left(a2, 6)
add_left(a1, 12)
print is_balanced(bt)

         #1
    #2           #3
 #4  #5       #6    #7  
       #11  #12
         #20
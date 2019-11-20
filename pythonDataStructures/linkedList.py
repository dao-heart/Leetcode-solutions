## Singled Linked List

class Node:
	def __init__(self,val):
		self.val = val
		self.next = None
	def traverse(self):
		node = self
		while node != None:
			print(node.val)
			node = node.next

class DoubleNode:
	def __init__(self,val):
		self.val = val
		self.prev = None
		self.next = None

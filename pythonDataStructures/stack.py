class Stack:
	def __init__():
		self.stack=[]
	def pop(self):
		if self.is_empty():
			return None
		else:
			return self.stack.pop()
	def push(self, element):
		return self.stack.append(element)
	def peak(self):
		if self.is_empty():
			return None
		else:
			return self.stack[-1]
	def size(self):
		return len(self.stack)
	def is_empty(self):
		return self.size() ==0
		

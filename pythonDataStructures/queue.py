class Queue:
	def __init__(self):
		self.queue = []
	def dequeue(self):
		if self.queue.is_empty():
			return None
		else:
			return self.queue.pop()
	def enqueue(self, val):
		return self.queue.insert(0,val)
	def size(self):
		return len(self.queue)
	def is_empty(self):
		return self.size==0
 

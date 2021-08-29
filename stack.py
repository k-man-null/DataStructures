class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return len(self.items) == 0

	def push(self, item):
		self.items.append(item)

	def pop(self):
		if self.isEmpty():
			return None
		else:
			return self.items.pop()

	def peek(self):
		return self.items[-1]

	def size(self):
		return len(self.items)

	def __repr__(self):
		status = "Printing Stack:\n"
		for i in range(self.size()-1, -1, -1):
			status+= str(self.items[i]) + "\n"
		status+= "---"
		return status


a = Stack()

print("Stack is empty :  ", a.isEmpty())
print("Adding items... ", a.push(4))
print("Adding items... ", a.push(14))
print("Adding items... ", a.push(8))

print("Stack size :  ", a.size())
print("Peeking the top item:  ", a.peek())

print(a)






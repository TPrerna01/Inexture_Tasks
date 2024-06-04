""" Implement Queue

You script should contain three functions

1. enqueue
2. dequeue
3. peek 

User will be given choice to perform action from above three.

Script should be kept running until user chooses to exit.		"""

from collections import deque

class Queue:
	""" Queue opeartion funct store"""
	def __init__(self):
		''' create an empty deque for 
			storing data '''
		self.conatiner = deque()

	def display(self):
		''' function for display option
			to user for operation list  '''
		option = """ 
					1 => enqueue
					2 => dequeue
					3 => peek
					4 => exit	"""
		while True:
			print(option)
			try:
				user_input = int(input("select the option from above : "))
				match user_input:
					case 1:
						self.enqueue()
					case 2:
						self.dequeue()
					case 3:
						self.peek()
					case 4:
						break
					case _:
						print("wrong input")
			except :
				print("only numbers  are allowed ")
				continue

	def enqueue(self):
		''' entering new data on queue'''
		item = input("enter new element : ")
		self.conatiner.append(item)
		print("add successfully")

	def dequeue(self):
		''' delete 1st data from the queue[front]'''
		try:
			self.conatiner.pop()
			print("remove data successfully")
		except :
			print("empty queue")

	def peek(self):
		''' print the lastdata form queue
			[rear]'''
		try: 
			data = self.conatiner[-1]
			print(data)
		except :
			print("empty queue")


if __name__=="__main__":
	queue_data = Queue()
	queue_data.display()
	
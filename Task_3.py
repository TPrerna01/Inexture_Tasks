"""Implement Circular Queue

You script should contain four functions

1. Front: Get the front item from queue.

2. Rear: Get the last item from queue.

3. enqueue(value)

4. dequeue()

User will be given choice to perform action from above four.

Script should be kept running until user chooses to exit."""

from collections import deque

class Circular_Queue:
	''' performing operation on circular queue'''
	def __init__(self):
		self.items = deque()

	def display(self):
		''' provide the operation option to user'''
		option = """
					1 => Front (get front item of queue)
					2 => Rear  (get last item of queue)
					3 => enqueue
					4 => dequeue	
					5 => exit			"""
		n = 5
		while True:
			print(option)
			try:
				user_input = int(input("Select option from above : "))
				match user_input:
					case 1 :
						self.front()
					case 2 :
						self.rear()
					case 3 :
						if len(self.items) < n:
							self.enqueue()
						else:
							print("Queue is full")
					case 4 :
						self.dequeue()
					case 5 :
						break
					case _ :
						print("invalid input")
			except :
				print("only numbers  are allowed ")
				continue

	def front(self):
		''' display the front element'''
		try :
			item = self.items[0]
			print(item)
		except :
			print("Empty Queue")

	def rear(self):
		''' display the last element'''
		try :
			item = self.items[-1]
			print(item)
		except :
			print("Empty Queue")
	
	def enqueue(self):
		''' entering new data on queue'''
		item = input("enter new element : ")
		self.items.append(item)
		print("add successfully")

	def dequeue(self):
		''' delete 1st data from the queue[front]'''
		try:
			self.items.pop()
			print("remove data successfully")
		except :
			print("empty queue")

if __name__=="__main__":
	circular_data = Circular_Queue()
	circular_data.display()
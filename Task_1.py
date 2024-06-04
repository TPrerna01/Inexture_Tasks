""" Implement Stack

Your script should contain three functions
1. push
2. pop
3. peep

User will be given choice to perform action from above three.

Script should be kept running until user chooses to exit.		"""

class Stack:
	''' holding Stack operation for list '''

	def __init__(self):
		''' creating and empty list for
			for storing stack data '''
		self.conatiner = list()

	def display(self):
		'''func for getting user choice '''
		option = """
					1 => Push
					2 => Pop
					3 => Peep   
					4 => exit   """
		while True:
			print(option)
			try:
				user_input= int(input("Enter choice from above list : "))

				match user_input:
					case 1:
						item_input = input("Enter new element : ")
						self.push(item_input)
					case 2:
						self.pop()
					case 3:
						total_item = len(self.conatiner)
						if total_item > 1:
							print("length of stack : 0 to",total_item-1)
							position = int(input("enter index no for get element : "))
							self.peep(position)
						else:
							self.peek()
					case 4:
						break
					case _ :
						print("wrong input")

			except :
				print("only numbers  are allowed ")
				continue

	def push(self, element):
		''' Adding Element On Stack '''
		self.conatiner.append(element)
		print("add successfully\n\n")

	def pop(self):
		''' Removing Last Element for Stack'''
		try:
			self.conatiner.pop(-1)
			print("remove item successfully\n\n")
		except Exception :
			print("List is Empty")

	def peep(self, position):
		try:
			data = self.conatiner[position]
			print(f"index {position} element is {data}")
		except Exception :
			print("Empty List")

	def peek(self):
		try:
			data = self.conatiner[-1]
			print(f"only element in list is {data}")
		except Exception :
			print("Empty List")
if __name__=="__main__":
	stack_data = Stack()
	stack_data.display()
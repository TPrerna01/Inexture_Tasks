class Factor:
	''' find the optimize number of factor'''

	def __init__(self):
		''' storing the number in an instance for factor '''
		self.factor = int(input("enter number to find the factor : "))

	def factor_data(self, data):
		''' opertion perform to perform factor task'''
		lst = []
		for i in range(1,  data):
			if data%i == 0:  
				lst.append(i)
		return lst

	def display(self):
		''' display the data of the factor'''
		ans = self.factor_data(self.factor)
		print(f" factor of the number {self.factor}")
		for i in ans:
			print(f"{i} ")

if __name__=="__main__":
	try:
		fact = Factor()
		fact.display()
	except:
		print("only one numbers allowed")
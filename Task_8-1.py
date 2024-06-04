''' 2 matrix of 3*3 multiply  '''
class MatrixOperation:
	''' hadle matrix data and operation method'''
	def __init__(self):
		self.matrix_1 = []
		self.matrix_2 = []
 
	def matrix_data(self):
		''' taking user input for matrix '''
		try:
			num = 2
			while num != 0:
				for i in range(3):
					user_input = list(map(int, input("enter 3 item for matrix use ' ' in between : ").split()))
					final_input = [item for item in user_input if user_input.index(item) < 3]
					if num > 1:
						self.matrix_1.append(final_input)
					else:
						self.matrix_2.append(final_input)
				num -= 1
			result = []
			for k in range(3):
				r = []
				for i in range(3):
					ans = []
					for j in range(3):
						ans1 = self.matrix_1[i][j] * self.matrix_2[i][j] 
						ans.append(ans1)
					r.append(sum(ans))
				result.append(r)
			return result

		except :
				print("only numbers are allowed")

	def display(self):
		ans = self.matrix_data()
		for item in ans:
			print(item)
		
if __name__=="__main__":
	matrix_record = MatrixOperation()
	matrix_record.display()
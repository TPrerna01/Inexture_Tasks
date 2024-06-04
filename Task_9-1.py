''' prog for finding the determinate of 3 * 3 matrix '''
class Matrix:
	''' store the matrix and determinate matrix method'''
	def __init__(self):
		''' matrix instance'''
		self.mylist = []

	def matrix_data(self):
		''' taking user input for matrix '''
		try:
			user_input = int(input("enter number of raw you want {must be <= 3} :"))
			for i in range(user_input):
				matrix_raw_input = list(map(int, input("enter 3 item for matrix use ' ' in between : ").split()))
				final_input = [item for item in matrix_raw_input if matrix_raw_input.index(item) < user_input]
				self.mylist.append(final_input)
		except :
				print("only numbers are allowed")

	def matrix_operation(self, matrix_1):
		''' work on determinant using loop and recursion '''
		try:
			size = len(matrix_1)
			raw_mat , col_mat = len(matrix_1), len(matrix_1[-1])
			if raw_mat == col_mat:
				for i in self.mylist:
					print(i)
				if size == 1:
					return matrix_1[0][0]
				elif size == 2:
					mat = ((matrix_1[0][0]* matrix_1[1][1]) - (matrix_1[1][0] * matrix_1[0][1]))
					return mat
				else:
					result = ( ((matrix_1[0][0]) * ((matrix_1[1][1] * matrix_1[2][2]) - (matrix_1[1][2] * matrix_1[2][1])))
						-((matrix_1[0][1]) * ((matrix_1[1][0] * matrix_1[2][2]) - (matrix_1[1][2] * matrix_1[2][0])))
						+((matrix_1[0][2]) * ((matrix_1[1][0] * matrix_1[2][1]) - (matrix_1[2][0] * matrix_1[1][1]))) ) 
					return result
			else:
				print("only work on square matrix which <= 3")
		except:
			pass

	def display(self):
		self.matrix_data()
		ans = self.matrix_operation(self.mylist)
		print(f"determinant is : {ans}")

if __name__ == "__main__":
	mat_data = Matrix()
	mat_data.display()
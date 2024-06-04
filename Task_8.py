''' 2 matrix of 3*3 multiply  '''
import numpy as np

class MatrixOperation:
	''' hadle matrix data and operation method'''
	def __init__(self):
		self.matrix_1 = np.array([])
		self.matrix_2 = np.array([])
 
	def matrix_data(self):
		''' taking user input for matrix '''
		mat1 = self.matrix_1
		mat2 = self.matrix_2
		try:
			num = 2
			while num != 0:
					print(f"\nmatrix data :\n")
					for i in range(3):
						for j in range(3):
							arr = int(input(f"enter matrix item {[i]}{[j]} : "))
							if num > 1:
								mat1 = np.append(mat1, [arr])
							else:
								mat2 = np.append(mat2, [arr])
					num -= 1

			result = np.dot(mat1.reshape((3, 3)), mat2.reshape((3, 3)))
			return result

		except :
				print("only numbers are allowed")
		finally:
			print("try again")

	def display(self):
		ans = self.matrix_data()
		print(ans)
		
if __name__=="__main__":
	matrix_record = MatrixOperation()
	matrix_record.display()
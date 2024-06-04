''' prog for finding the determinate of 3 * 3 matrix '''
import numpy as np

class Matrix:
	''' store the matrix and determinate matrix method'''
	def __init__(self):
		''' matrix instance'''
		self.mylist = np.array([])

	def matrix_data(self):
		''' taking user input for matrix '''
		mat = self.mylist
		try:
			print(f"\nmartix  : \n")
			for i in range(3):
				row = []
				for j in range(3):
					arr = int(input(f"enter matrix 1 item {[i]}{[j]} : "))
					row.append(arr)
				mat = np.append(mat, 	row)
			
			return mat.reshape((3, 3))
		except :
				print("only numbers are allowed")
		finally:
			print("try again")

	def matrix_operation(self):
		matrix_1 = self.matrix_data()
		try:
			result = np.linalg.det(matrix_1)
			return result
		except:
			pass

	def display(self):
		ans = self.matrix_operation()
		print(ans)

if __name__ == "__main__":
	mat_data = Matrix()
	mat_data.display()
""" 
1    2    3    4
12  13  14  5
11  16  15  6
10  9    8    7"
"""
class Spiral_Matrix:
	def number_arrange_pattern(self, n, m, matrix):
		""" taking  userinput for number of lines and buliding an loop for diaplaying square """
		top, bottom = 0,0
		value  = 1
		while (top <= m and bottom <= n):
			for i in range(bottom, n):
				matrix[top][i] = value
				value += 1
			top += 1

			for i in range(top, m):
				matrix[i][n-1] = value
				value += 1
			n -= 1
			if (top <= m):
				for i in range(n - 1, bottom - 1, -1):
					matrix[m - 1][i] = value
					value += 1
				m -= 1
			if (bottom <= n):
				for i in range(m - 1, top - 1, -1):
					matrix[i][bottom] = value
					value += 1
				bottom += 1
		return matrix

	

	def display(self, num):
		""" displaying the spiral matrix to user """
		n, m = num, num
		a = [[0 for i in range(n)] for j in range(m)]
		self.number_arrange_pattern(n, m, a)
		for i in range(n):
			for j in range(m):
				print(a[i][j], end= " ")
			print()

if __name__=="__main__":
	try:
		user_input = int(input("enter number of a line you want in triangle : "))
		if user_input > 0 :
			spiral = Spiral_Matrix()
			spiral.display(user_input)
		else:
			print("only positive numbers allowed")
	except:
		print(f"only numbers allowed")
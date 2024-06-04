""" 
           1
         1   1
       1   2   1
     1   3   3    1
   1  4    6   4   1
 1  5   10   10  5   1"
"""
def pasal_triangle(num):
	"""printing  numbers on pascal_triangle  """
	ps = []
	for i in range(num):
		temp = []
		for j in range(i+1):
			if j == 0 or j == i:
				temp.append(1)
			else:
				temp.append(ps[i-1][j-1] + ps[i-1][j])
		ps.append(temp) 

	for i in range(num):
		for j in range(num-i-1):
			print(" ", end ="")
		for j in range(i+1):
			print(ps[i][j], end =" ")
		print()
	
if __name__=="__main__":
	try:
		user_input = int(input("enter number of a line you want in triangle : "))
		if user_input > 0 :
			pasal_triangle(user_input)
		else:
			print("only positive numbers allowed")
	except:
		print(f"only numbers allowed")
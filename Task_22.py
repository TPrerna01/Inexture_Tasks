"""
        1
      2 3 2
    3 4 5 4 3
  4 5 6 7 6 5 4
5 6 7 8 9 8 7 6 5"
"""
def triangle_4(num):
	"""printing  numbers on pattern _triangle  """
	a = 1
	g = num -1
	for i in range(1, num):
		a = i
		for j in range(1, g):
			print(" ", end = " ")
		g -=1	
		for j in range(1, i+1):
			print(a, end = " ")
			a += 1
		a-= 2
		for j in range(1, i):
			print(a,end =" ")
			a -= 1
		print()

if __name__=="__main__":
	try:
		user_input = int(input("enter number of a line you want in triangle : "))
		if user_input > 0 :
			triangle_4(user_input)
		else:
			print("only positive numbers allowed")
	except:
		print(f"only numbers allowed")
"""
1
2 3
4 5 6
7 8 9 10"
"""

def triangle_4(num):
	"""printing numbers on right angle triangle  """
	n = 1
	for i in range(1,num+1):
		m = i+n
		print(*range(n,m))
		n += i
		
if __name__=="__main__":
	try:
		user_input = int(input("enter number of a line you want in triangle : "))
		if user_input > 0 :
			triangle_4(user_input)
		else:
			print("only positive numbers allowed")
	except:
		print(f"only numbers allowed")
"""
"1
1 2
1 2 3
1 2 3 4
1 2 3 4 5"
"""
def right_angle_triangle(num):
	"""printing numbers on right angle triangle  """
	j = str()
	for i in range(1,num+1):
		j += ''.join(str(i))
		print(f"{j}")
	

if __name__=="__main__":
	try:
		user_input = int(input("enter number of a line you want in triangle : "))
		if user_input > 0 :
			right_angle_triangle(user_input)
		else:
			print("only positive numbers allowed")
	except:
		print(f"only numbers allowed")
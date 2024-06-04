"""1 2 3 4 5
1 2 3 4 
1 2 3
1 2
1"" 

"""
def triangle_2(num):
	"""printing triangle  """
	for i in reversed(range(1,num+1)):
		print(*range(1,i+1))
		

if __name__=="__main__":
	try:
		user_input = int(input("enter number of a line you want in triangle : "))
		if user_input > 0 :
			triangle_2(user_input)
		else:
			print("only positive numbers allowed")
	except:
		print(f"only numbers allowed")
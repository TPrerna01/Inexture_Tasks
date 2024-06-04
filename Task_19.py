"""
"* * * * *
* * * *
* * * 
* *
*"
"""
def triangle_1(num):
	"""printing triangle  """
	for n in reversed(range(1,num+1)):
		print(n * '*')

if __name__=="__main__":
	try:
		user_input = int(input("enter number of a line you want in triangle : "))
		if user_input > 0 :
			triangle_1(user_input)
		else:
			print("only positive numbers allowed")
	except:
		print(f"only numbers allowed")
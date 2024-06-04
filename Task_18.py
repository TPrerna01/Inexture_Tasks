"""
"A
B B
C C C
D D D D
E E E E E"
"""

def alpha_triangle(num):
	"""printing alphabate using ascii on triangle  """
	n = 65
	for i, char in enumerate(range(n, n+num), start = 1):
		print(i * chr(char))
	

if __name__=="__main__":
	try:
		user_input = int(input("enter number of a line you want in triangle : "))
		if user_input > 0 :
			alpha_triangle(user_input)
		else:
			print("only positive numbers allowed")
	except:
		print(f"only numbers allowed")
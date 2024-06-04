""" 
*
* *
* * *
* * * *
* * * * *		"""

def triangle(num):
	""" printing stars on triangle using loops """
	for n in range(1, num+1):
		print(f"{n * '*'} ")

if __name__=="__main__":
	try:
		user_input = int(input("enter number of a line you want in triangle : "))
		if user_input > 0 :
			triangle(user_input)
		else:
			print("only positive numbers allowed")
	except:
		print(f"only numbers allowed")

""" 
"        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *"
"""
def equilateral_triangle(num):
	"""printing equilateral_triangle  """
	for i in range(1, num+1):
		print(f"{((i-1) * '*').rjust(num)}{i * '*'}")
	
if __name__=="__main__":
	try:
		user_input = int(input("enter number of a line you want in triangle : "))
		if user_input > 0 :
			equilateral_triangle(user_input)
		else:
			print("only positive numbers allowed")
	except:
		print(f"only numbers allowed")
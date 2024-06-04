""" 
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
"""
def equilateral_triangle_2(num):
	"""printing equilateral_triangle upside down """
	for i in reversed(range(1, num+1)):
		print(f"{((i-1) * '*').rjust(num)}{i * '*'}")
	
if __name__=="__main__":
	try:
		user_input = int(input("enter number of a line you want in triangle : "))
		if user_input > 0 :
			equilateral_triangle_2(user_input)
		else:
			print("only positive numbers allowed")
	except:
		print(f"only numbers allowed")
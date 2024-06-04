def diamond_pattern(num):
	""" taking num of line user want and using loop for diaplaying diamond """
	for i in range(1, num+1):
		n = i * '+'
		print(f"{str(n).rjust(num)}{(i-1) * '+'}")
	for j in reversed(range(1, num)):
		n = j * '+'
		print(f"{str(n).rjust(num)}{(j-1)* '+'}")

if __name__=="__main__":
	try:
		user_input = int(input("enter number of a line you want in triangle : "))
		if user_input > 0 :
			diamond_pattern(user_input)
		else:
			print("only positive numbers allowed")
	except:
		print(f"only numbers allowed")
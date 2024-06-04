# palindrome number

class Palindrom:
	''' used to find the palindrom number'''

	def __init__(self):
		''' Taking user input'''
		self.user_input = input("enter data : ")

	def data_convertion(self):
		''' reversing user input'''
		try:
			number = int(self.user_input)
			if number: 
				convert_data = self.user_input[::-1]
				return convert_data
		except :
			print("only numbers allowed")

	def check_palindrome(self):
		''' code for checking the palindrom data'''
		try:
			if self.data_convertion()  is not None:
				if self.user_input == self.data_convertion():
					print(f"{self.user_input} is palindrome")
				else :
					print(f"{self.user_input} is not palindrome")
		except:
			return None

if __name__=="__main__":
	Palindrom_data = Palindrom()
	Palindrom_data.check_palindrome()
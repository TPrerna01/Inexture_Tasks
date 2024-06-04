# cow and bull game

from random import choices

class Guessing_Game:
	''' store the method for generting random number and taking user_input
	for comapring the number and giving the hint'''

	def __init__(self):
		''' storing auto generating number on instance '''
		self.auto_number = choices([1,2,3,4,5,6,7,8,9,0], k=4)

	def user_data(self):
		''' taking user input '''
		user_input_item = input("enter 4-digit number : ")
		user_input = [int(item) for item in user_input_item]
		return user_input

	def user_guess(self):
		''' method for checking the user guess and original number'''
		flag = True
		no_guess = 0
		while flag:
			try:
				user_input = self.user_data()
				no_guess += 1
				cow = 0
				bull = 0
				if len(user_input) == 4:
					if user_input == self.auto_number:
						print(f"Total number of user guess is {no_guess}")
						flag = False
					else:
						for i,item in enumerate(self.auto_number):
							if user_input[i] is item:
								cow += 1
							elif user_input[i] in self.auto_number:
								if user_input[i] is not self.auto_number:
									bull += 1
						print(f"cow : {cow} , bull : {bull}")
				else:
					print("len of input must be 4.\n")
			except:
				print("invalid input or format")				

if __name__=="__main__":
	guess_game = Guessing_Game()
	guess_game.user_guess()
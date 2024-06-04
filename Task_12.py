""" "Create an ATM machine

- User should be able get money out of it
- User should be able to deposite money into it
- You must ask card number and pin before any transaction
- User can get overall information about his bank account
- There should be a limit in one time transaction and total transaction in a day (Consider day as from starting of script to exit)
- Limit on number of transaction
- Let user choose the bank of ATM
- Every ATM will have some initial balance
- Every user has it's own bank
- If user takes money from an ATM other than his bank take 5% cut in withdrawl amount

Nice to have features:
- Insert, update and delete users (Generate card number and PIN randomly)
- Insert, update and delete ATMs
- Insert, update and delete banks
- Insert money into ATM (No database is needed for this it can be managed using dicts)

Hint: You can manage all this with data dictionary data type."		"""

from random import randint

class Main:
	''' Atm machine service method for user & admin '''
	def __init__(self):
		''' atm_data store the atm data and bank data also default value for testing '''
		self.admin = {'admin@gmail.com' : "adminworld"}
		self.atm_data = {'asd' : ['y', 15000], 'xyz' : ['y', 20000], 'qwe' : ['n']}
		self.user_data = {10000 : ['asd', 1000200033, 'natasa', 1111, 5000], 10001 : ['xyz', 1000200034, 'neha', 2222, 4000]}

	def add_atm_details(self):
		''' atm and bank data added '''
		while True:
			atm_bank = input("enter bank name : ")
			atm_confirmation = input("want to open an atm for above bank [y/n] : ")
			self.atm_data[atm_bank] = [atm_confirmation]
			if atm_confirmation == 'y':
				atm_balance = int(input("enter balance on atm : "))
				self.atm_data[atm_bank].append(atm_balance)
				print("atm record add successfully.")
			elif atm_confirmation == 'n':
				pass
			else:
				print("invalid data")
			user_permission = input("continue add atm and bank data [y/n] : ")
			if user_permission == 'y':
				pass
			elif user_permission == 'n':
				break
			else:
				print("invalid data")

	def isempyt(self,data):
		''' check empty data '''
		try:
			if data == None or len(data) == 0:
				return True
		except:
			return False 

	def display_atm_data(self):
		''' for displaying atm data for admin'''
		print("\n atm data list :\n")
		print(f"Atm bank-#-money on Atm")
		for i in self.atm_data.items():
			if 'y' in i[1]:
				print(f" {i[0]}\t{i[1][1]}")

	def display_bank_list(self):
		''' display bank list for user '''
		print("\nbank list :")
		print(f"bank name =>")
		for item in self.atm_data:
				print(f" {item}")

	def add_user(self):
		''' adding user data '''
		print("adding new user data")
		while True:
			self.display_bank_list()
			account_no = randint(10000,99999)
			user_bank = input("enter bank name : ")
			card_no = randint(1000000000, 9999999999)
			user_name = input("enter user name : ")
			pin_no = randint(1000, 9999)
			if user_bank in self.atm_data.keys() :
				if (not self.isempyt(user_name) 
						and not self.isempyt(user_bank)):
					self.user_data[account_no] =  [user_bank, card_no, user_name, pin_no]
					print("user data submitted successfully")
			else:
				print(f"invalid bank name {user_bank}")
			user_permission = input("want to continue adding user [y/n] :")
			if user_permission == 'y':
				continue
			elif user_permission == 'n':
				break
			else:
				print("invalid data")

	def change_user_details(self):
		''' change the bank and user name '''
		user_account_no = int(input("enter user card no :"))
		user_name = input("enter name :")
		user_bank = input("enter bank name :")
		if not self.isempyt(user_name) and not self.isempyt(user_bank):
			self.user_data[user_account_no][0:3:2] = [user_bank, user_name]
		elif not isempyt(user_name) and self.isempyt(user_bank):
			self.user_data[user_account_no][2] = [ user_name]
		elif not isempyt(user_bank) and self.isempyt(user_name):
			self.user_data[user_account_no][0] = [ user_bank]
		print("update successfully")

	def change_atm_details(self):
		''' add atm on bank and updatae balance '''
		option_1 = ''' 1 =>  provide atm to bank  \t2 => update balance '''
		print(option_1)
		user_input = int(input("select option :"))
		match user_input:
			case 1:
				print("\nlist of bank which have no atm")
				print(f" Bank Name :")
				for item in self.atm_data.items():
					if 'n' == item[1][0]:
						print(item[0])
				else:
					print("no other data")
				atm_bank_name = input("enter bank name :")
				atm_balance = int(input("enter atm balance :"))
				self.atm_data[atm_bank_name] = ['y', atm_balance]
				print("update successfully")

			case 2:
				self.display_atm_data()
				atm_bank = input("enter name : ")
				balance = int(input("enter amount :"))
				self.atm_data[atm_bank][1] = balance
				print("update successfully")
			case _:
				print("invalid data")

	def change_data(self):
		''' calling the method of updating for user and atm '''
		option = ''' 
				\r1 => change user data  \t2 => change atm data  \t3 => exit			'''
		while True:
			try:
				print(option)
				admin_input = int(input("select option : "))
				match admin_input:
					case 1:
						print("CHANGE USER_BANK AND USER_NAME ON RECORDS")
						self.change_user_details()
					case 2:
						print("ALLOW BANK TO ATM AND PROVIDE BALANCE")
						self.change_atm_details()
					case 3 :
						break
					case _ :
						print("invalid input")
			except:
					print("only numbers allowed")

	def remove_user_details(self):
		''' permanentely deleting user data'''
		user_account_no = int(input("enter account no :"))
		del self.user_data[user_account_no]
		print(f"delete user {user_account_no} from data")

	def remove_atm_details(self):
		''' delete bank and atm from data'''
		bank_name = input("enter name :")
		del self.atm_data[bank_name]
		print(f"delete the {bank_name} from data ")

	def remove_details(self):
		''' user data and atm ,bank data remove method calling '''
		option = ''' 
				\r1 => delete user data  \t2 => delete atm & bank data  \t3 => exit			'''
		while True:
			try:
				print(option)
				admin_input = int(input("select option : "))
				match admin_input:
					case 1:
						print("DELETE USER RECORD FROM DATA")
						self.remove_user_details()
					case 2:
						print("DELETE BANK & ATM DATA FROM RECORDS ")
						self.remove_atm_details()
					case 3:
						break
					case _:
						print("invalid input")
			except:
					print("only numbers allowed")

	def display_user_details(self, user_account_no = None): 
		''' display user data '''
		if not self.isempyt(user_account_no):
			print(f"\naccount_no : {user_account_no}")
			data = ['Bank', 'card_no', 'User', 'Pin_no', 'Balance']
			for i, item in enumerate(self.user_data[user_account_no]):
				print(f"{data[i]}   :   {item}")
		else:
			print("\nUSER ACCOUNT_NO LIST:")
			for i, item in enumerate(self.user_data.keys(), start = 1):
				print(f" {i} : {item}")


	def deposit_money(self, user_account_no):
		''' deposit user money method'''
		user_deposit = int(input("enter amount : "))
		if len(self.user_data[user_account_no]) > 4:
			self.user_data[user_account_no][4] += user_deposit
		else:                     
			self.user_data[user_account_no].append(user_deposit)
		print(f"{user_deposit} Rs on your account {user_account_no} successfully.")

	def withdrawl_money(self, bank_name, user_account_no):
		''' valiadation and condition for user to withdrawl money from account'''
		use_time = 0
		pin_no = int(input("enter pin_no : "))
		amount = int(input("enter the withdrawl amount :"))
		if (self.user_data[user_account_no][3] == pin_no ) :
			if ( amount <= 20000) : 
				if (len(self.atm_data[bank_name]) > 1
						and self.atm_data[bank_name][1] >= amount):
					if use_time <= 3:
						if len(self.user_data[user_account_no]) > 4:
							if self.user_data[user_account_no][4] >= amount :
								self.user_data[user_account_no][4] -= amount
								print(f"{self.user_data[user_account_no][4]} remaing balance" )
								if (self.user_data[user_account_no][0] != bank_name):	
									use_time += 1
									print(f"\n{{ 5% charge }} for using {bank_name} atm will deduct.")
									print(f"your withdrawl money is {amount-amount*5/100}\n")
									self.atm_data[bank_name][1] -= amount*5/100
								else:
									use_time += 1
									print(f"\nyour withdrawl money is {amount}")
									self.atm_data[bank_name][1] -= amount
							else:
								print(f"Not enough amount in your account")
						else:
							print(f"{user_account_no} has 0 balance")
					else:
						print("only 3 time transcation allowed in 1 day ")
				else:
					print("atm have not sufficient balance")
			else:
				print(f"withdrawl limit {{20000/-}}")
		else:
			print("invalid pin_no ")

	def user_service(self):
		''' user service & limit condition for using atm '''
		option = f''' 
				\r1 => deposit money   \n2 => credit money(withdrawl)    \n3 => view account infomation     \n4 => exit'''
		self.display_bank_list()
		bank_name = input("enter the bank name for using atm service :")
		user_card_no = int(input("enter card no : "))
		ans = {key:value for key, value in self.user_data.items() if user_card_no in value}
		user_account_no = list(ans.keys())[0]
		if (user_card_no == list(ans.values())[0][1]
				and bank_name in self.atm_data):
			print(f"welcome {user_card_no} on Atm service of {bank_name} bank")
			while True:
				try:
					print(option)
					user_input = int(input("choose from above option :"))
					match user_input:
						case 1:
							print("DEPOSIT YOUR MONEY")
							self.deposit_money(user_account_no)
						case 2:
							print("WITHDRAWL MONEY")
							self.withdrawl_money(bank_name, user_account_no)	
						case 3:
							self.display_user_details(user_account_no)
						case 4:
							break
						case _:
							print("invalid data")
				except:
					print("only numbers allowed")
		else:
			print(f"enter valid data")

	def admin_login(self):
		''' admin login method '''
		option = f'''1 => add atm and bank data   \n2 => add user data    \n3 => update atm or user data  \n4 => display atm data    
				\r5 => display bank data     \n6 => display user data     \n7 => delete atm & user data     \n8 => exit   '''
		# admin_name = input("enter your email-id : ")
		# password = input("enter your password :")
		# if (admin_name in self.admin and password in self.admin.values()) :
		while True:
			try:
				print(option)
				admin_input = int(input("select from above option :"))
				match admin_input:
					case 1:
						self.add_atm_details()
					case 2:
						self.add_user()
					case 3:
						self.change_data()
					case 4:
						self.display_atm_data()
					case 5:
						self.display_bank_list()
					case 6:
						print(f" 1 => USER ACCOUNT_NO LIST \t 2 => USER ACCOUNT_DETAILS  \t 3 => exit")
						admin_input = int(input("choose from above option : "))
						match admin_input:
							case  1:
								account_no = int(input("enter account_no : "))
								self.display_user_details(account_no)
							case 2:
								self.display_user_details()
							case 3:
								break 
					case 7:
						self.remove_details()
					case 8:
						break
					case _:
						print("invalid input")
			except:
				print("only numbers allowed")

	def home_access(self):
		''' user & admin service access method '''
		option = ''' 
				1 => if user     \n\t\t\t\t2 => if admin    \n\t\t\t\t3 => exit		'''
		while True:
			try:
				print(option)
				user_input = int(input("access service as : "))
				match user_input:
					case 1:
						print("USER SERVICES")
						self.user_service()
					case 2:
						print("ADMIN SERVICE")
						self.admin_login()
					case 3:
						break
					case _:
						print("invalid input")
			except:
					print("only numbers allowed")

if __name__=="__main__":
	main = Main()
	main.home_access()
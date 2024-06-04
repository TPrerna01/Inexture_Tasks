class LCM_GCD:
	''' lcm and gcd function '''
	def __init__(self):
		''' using instance to store the value '''
		self.value = list(map(int, input("enter value using 'space' in between to find lcm & gcd  :"). split()))

	def lcm_opreation(self):
		''' opertion perform to find the lcm of given numbers'''
		if all(item >=0 for item in self.value):
			n = 1
			while True:
				val = self.value[0] * n
				if all(val%items==0 for items in self.value): 
					lcm = val
					break
				n += 1
			return lcm

	def gcd_opeartion(self):
		''' take the lcm method data to find the gcd '''
		gcd = 1
		data = [gcd:=gcd*num for num in self.value]
		result = gcd//self.lcm_opreation()
		return result

	def display(self):
		values = self.value
		print(f"lcm : {self.lcm_opreation()}")
		print(f"gcd : {self.gcd_opeartion()}")

if __name__=="__main__":
	try:
		lcm = LCM_GCD()
		lcm.display()
	except:
		print("only positive numbers allowed")
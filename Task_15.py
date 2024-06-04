class ARRANGE_ARRAY:
	''' perform task for rearraging the array'''
	def __init__(self):
		''' instance for storing array input and removing negative & duplicate value '''
		self.array = list(map(int, input("enter value using 'space' in between : ").split()))
		self.final_arr = [ item for i, item in enumerate(self.array) if item >= 0 and item not in self.array[:i]]
		
	def rearrange_operataion(self, array_1):
		''' creating a[i] and rearranging as a[a[i]]'''
		try:
			array_data1 = [array_1[i] for i in array_1]
			rearrange_data = [array_1[array_1[i]]  for i in array_data1]
			return rearrange_data
		except:
			print("length of the number should be highest positive value u of your input (without duplicate)")

	def display(self):
		''' display the rearrange_array data'''
		ans = self.rearrange_operataion(self.final_arr)
		print(ans)

if __name__=="__main__":
	try:
		arrangeing_data = ARRANGE_ARRAY()
		arrangeing_data.display()
	except:
		print("only numbers allowed")
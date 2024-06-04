''' In Binary Search the mid value find
	using low & high index continue until keyfound'''

class Binary:
	''' binary search method store'''

	# def __init__(self,items, key_value):
	# 	''' list for binary search '''
	# 	self.mylist = items
	# 	self.value = key_value

	def __init__(self, key_value):
		''' instance arr for binary search '''
		self.mylist = [26, 54, 93, 17, 77, 31, 44, 55, 1, 20]
		self.value = key_value

	def insertion_sort(self):
		'''insertion sort logic & index ele swaping '''
		arr1 = self.mylist
		for i in range(len(arr1)):
			for j in range(len(arr1)-1):
				if arr1[j] >= arr1[j+1]:
					arr1[j], arr1[j+1] = arr1[j+1], arr1[j]

		return arr1

	def binary_search(self):
		''' use loop for search '''
		arr = self.insertion_sort()
		value = self.value
		l = 0
		h = len(arr)-1
		mid = l+(h-l)//2
		while l < h:
			if value == arr[mid]:
				return f"index {mid} : value {value}"
				
			elif value < arr[mid]:
				h, mid  = mid-1, l+(h-l)//2
				if value == arr[mid]:
					return f"index {mid} : value {value}"
				elif value < arr[mid]:
					h, mid  = mid-1, l+(h-l)//2
					if value == arr[mid]:
						return f"index {mid} : value {value}"
				elif value > arr[mid]:
					l, mid  = mid+1, l+(h-l)//2
					if value == arr[mid]:
						return f"index {mid} : value {value}"					

			elif value > arr[mid]:
				l, mid  = mid+1, l+(h-l)//2
				if value == arr[mid]:
					return f"index {mid} : value {value}"
				elif value < arr[mid]:
					h, mid  = mid-1, l+(h-l)//2
					if value == arr[mid]:
						return f"index {mid} : value {value}"
				elif value > arr[mid]:
					l, mid  = mid+1, l+(h-l)//2
					if value == arr[mid]:
						return f"index {mid} : value {value}"
	
		else:
					return f"value {value} : not in records"
			

	def display(self):
		''' method just to print sorted arr '''
		ans = self.binary_search()
		print(ans)

if __name__=="__main__":
	try:

		# user_input = list(map(int, input("enter arr list using space : ").split()))
		search_key = int(input("enter item val for search : "))
		# binary_data = Binary(user_input,search_key)
		binary_data = Binary(search_key)
		binary_data.binary_search()	
		binary_data.display()
	except:
		print("only numbers allowed")





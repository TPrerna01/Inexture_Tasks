''' In bubble the 1st ele select &
	campare to next for all the ele on it
	and the max ele will store onn the right 
	and the compare ele channge index with 
	original'''

class Bubble:
	''' storing the method for bubble sort '''

	# def __init__(self,items):
	# 	''' create an static list on constructer'''
	# 	self.mylist = items

	def __init__(self):
		self.mylist = [26, 17, 93, 55, 64]

	def bubble_sort(self):
		''' method for sorting arr '''
		arr = self.mylist
		for i in range(len(arr)):
			for j in range(len(arr)-1): 
				max_item = j       # [-1] so the loop do not show index error
				if arr[max_item] > arr[j+1] :    # comparing item
					max_item = j
					arr[max_item], arr[j+1] = arr[j+1], arr[max_item]   # swaping

		return arr

	def display(self):
		''' method just to print sorted arr '''
		ans = self.bubble_sort()
		print(ans)

if __name__=="__main__":
	# user_input = list(map(int, input("enter arr list using space : ").split()))
	# a = list(reversed(range(100)))
	# b = list(range(50,200))
	# a.extend(b)
	# user_input = a 
	# bubble_data = Bubble(user_input)
	bubble_data = Bubble()
	bubble_data.display()
''' In Selection sort the 1st ele compare to next
	and if find the min ele use that ele for compare
	futher after complete whole list it store the min ele on right
	# index ele swap procedure'''

class Selection:
	''' selection sort method  is used to sort 
		the list '''
	def __init__(self,items):
		''' create an static list on constructer'''
		self.mylist = items

	# def __init__(self):
	# 	''' create an static list on constructer'''
	# 	self.mylist = [26, 54, 93, 17, 77, 31, 44, 55, 1, 20]


	def selection_sort(self):
		''' function that sorting the list '''
		arr = self.mylist
		for i in range(len(arr)):
			m_item = i
			for j in range(i+1, (len(arr))):
				# print(arr[j])
				if arr[j] < arr[m_item]:
					m_item = j	
			arr[m_item],arr[i] = arr[i],arr[m_item]
				
		return arr

	def display(self):
		''' method just to print sorted arr '''
		ans = self.selection_sort()
		print(ans)

if __name__=="__main__":
	# user_input = list(map(int, input("enter arr list using space : ").split()))
	a = list(reversed(range(100)))
	b = list(range(50,200))
	a.extend(b)
	user_input = a 
	# user_input.append(a)
	# print(user_input)
	select_data = Selection(user_input)
	# select_data = Selection()
	select_data.display()
''' In insertion sort swaping from the start
	1st ele comapre to another if short pre
	index swap logic use '''

class Insertion:
	''' Insertion sort method hold '''

	# def __init__(self,items):
	# 	''' create an static list on constructer'''
	# 	self.mylist = items

	def __init__(self):
		self.mylist = [26, 17, 93, 25, 10]

	def insertion_sort(self):
		'''insertion sort logic & index ele swaping '''
		arr = self.mylist
		for i in range(len(arr)):
			for j in range(len(arr)-1):
				if arr[j] > arr[j+1]:
					arr[j], arr[j+1] = arr[j+1], arr[j]
					print(arr)

		return arr

	def display(self):
		''' method just to print sorted arr '''
		ans = self.insertion_sort()
		print(ans)

if __name__=="__main__":
	# user_input = list(map(int, input("enter arr list using space : ").split()))
	# a = list(reversed(range(0, 100,2)))
	# b = list(range(50,200,5))
	# a.extend(b)
	# user_input = a
	# insertion_data = Insertion(user_input)
	insertion_data = Insertion()
	insertion_data.display()
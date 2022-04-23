numbers=[1,2,3,4,5]
print(numbers.pop())       # returns the last element of the list (if no args)
print(numbers)
print(numbers.pop(1))       # returns the removed element from teh list: SYntax: list.pop(index)
print(numbers)
# Output:
# 5
# [1, 2, 3, 4]
# 2
# [1, 3, 4]
numbers=[1,2,3,4,5]
# numbers.clear()         # removes all the elements of the list and returns an empty list
numbers=[]
print(numbers)
numbers=[1,2,3,4,5]
num=[6,7,8,9]
numbers.extend(num)     # firstList.extend(secondList)
print(numbers)          # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Concatenation
numbers=[1,2,3,4,5]
num=[6,7,8,9]
print(numbers+num)      # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# insert
numbers=[1,2,3,4,5]
numbers.insert(3, 10)   # list.insert(index, element)
print(numbers)

'''
Methods	Descriptions
append()	adds an element to the end of the list
extend()	adds all elements of a list to another list
insert()	inserts an item at the defined index
remove()	removes an item from the list
pop()	returns and removes an element at the given index
clear()	removes all items from the list
index()	returns the index of the first matched item
count()	returns the count of the number of items passed as an argument
sort()	sort items in a list in ascending order
reverse()	reverse the order of items in the list
copy() 	returns a shallow copy of the list
'''

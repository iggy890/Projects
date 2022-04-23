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

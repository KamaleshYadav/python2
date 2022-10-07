# Method : 1 using slicing technique

# mylist = [2,5,8,94,4]
# mylist_copy = mylist[:]
# print(mylist_copy)

# Method : 2 using extend() method

# mylist = [2,5,8,94,4]
# mylist_copy = [10]
# mylist_copy.extend(mylist)
# print(mylist_copy)

# Method : 3 using list() method 

mylist = [2,5,8,94,4]
mylist_copy = list(mylist)
print(mylist_copy)

# Method : 4 using copy() method

mylist = [2,5,8,94,4]
mylist_copy = mylist.copy()
print(mylist_copy)

# Method : 5 using list comprehension

mylist = [2,5,8,94,4]
mylist_copy = [i for i in mylist]
print(mylist_copy)
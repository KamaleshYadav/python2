# Method : 1 clear method


# mylist = [4,5,8,9]
# print("Mylist before clear: ",mylist)

# mylist.clear()
# print("Mylist after clear: ",mylist)


# Method : 2 initializes the list with no value
# mylist = [4,5,8,9]
# print("Mylist before clear: ",mylist)

# mylist = []
# print("Mylist after clear: ",mylist)


#Method : 3 using "*=0" this method removes all element of the list andmakes it empty.
# mylist = [4,5,8,9]
# print("Mylist before clear: ",mylist)

# mylist *= 0
# print("Mylist after clear: ",mylist)


#Method : 4 using del method
mylist = [4,5,8,9,7]
print("Mylist before clear: ",mylist)

del mylist[:]
print("Mylist after clear: ",mylist)
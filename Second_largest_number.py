# Method 1 : using sorting

mylist = [3,64,33,67,65]

mylist.sort()

print(mylist[-2])

# Method 2 : using max() function

mylist.remove(max(mylist))

print(max(mylist))

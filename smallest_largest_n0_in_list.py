# Method 1 : using sorting

mylist = [13,20,5,89]

# mylist.sort()

# print(mylist)

# print(mylist[0])
# print(mylist[-1])


# Method 2 : using min and max method


# print(min(mylist))

# print(max(mylist))

# Method 3 : using loop

max = mylist[0]

for i in mylist:
    if i > max:
        max = i
print(max)


min = mylist[0]
for j in mylist:
    if j < min:
        min = j
        print(min)

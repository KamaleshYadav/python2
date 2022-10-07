# Find sum element in list

# Method1: using for loop with range()

mylist = [5,10,20]

total=0
l = len(mylist)

for i in range(0,l):
    total = total+mylist[i]
print(total)   


print(sum(mylist))
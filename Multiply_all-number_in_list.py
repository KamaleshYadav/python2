# list = [3,2,4]
# output = 24

# Method1: Traversal

mylist = [3,2,4]

result = 1

for x in mylist:
    result = result * x    #3 , 6 , 24

print(result)    


# Method 2 = using numpy.prod()   install numpy package

import numpy

mylist1 = [3,2,4]

result = numpy.prod(mylist1)  

print(result)                     

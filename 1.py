##print("Hello World")
##import math
##print(math.floor(3.65))
##print("this will run")

##a = 1
##b = 3
##print(a + b)

##c = ("This is string")
##print(c)
##d = 4.3
##print(type(d))

##str1 = "this is my first python string"
##print(str1.capitalize())
##print(str1.find("is"))
##print(str1.lower())
##print(str1.upper())

##List = ["raj",1,2,3]
##print(List)
##print(type(List))
##List[1] = "kgf"
##print(List)

##Tuple = (1,2,3) #Tuple can not be change
##print(Tuple)
##print(type(Tuple))
##
##dict1 = {}
##print(type(dict1))
##
##dict1["virat"] = 100
##dict1["Sachin"] = 500
##print(dict1)
##print(dict1.items())
##print(dict1.keys())

##l = [1,2,3,3,4]
##s= set(l)
##print(s)

##a = 10
##b = 5
##c = "Harry"
##print(str(a)+str(b)+c)
##print(a ,b , c)
##print("10 - 5 is ", 10-5)

##var = int(input())
##print(var)
##if(var>4):
##    print("Variable is greater")
##
##elif(var == 0):
##    print("Variable is zero")
##    
##else:
## print("Variable is not greater")

##for i in range (0, 100):
##    print(i)
##
##j = 0
##while(j<50):
##    print(j)
##    j+=1

##
##def average(num1, num2):
##    avr = (num1 + num2) / 2
##    return avr
##print(average(4,6))

##
##index = 3
##try:
##    print(index)
##except Exception as e:
##    print(e)



file = open("2.txt", "w")
file.write("raj")
file.close()

file1 = open("2.txt", "r")
c = file1.read()
file.close()
print(c)

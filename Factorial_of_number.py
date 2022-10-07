# Method : 1 

# factorial = 1
# num = 5

# if(num<0):
#     print("Factorial does not exist for nagative number")
# elif num ==0:
#     print(" The Factorial of 0 is 1")

# else:
#     for i in range(1,num+1):
#         factorial = factorial * i
#     print("The Factorial of ",num, "is", factorial)

#Method : 2
# num = int(input("Enter The Number: "))

# def fac(num):
#     if(num==0 or num==1):
#         return 1
#     else:
#         return num * fac(num-1)
# # num = 5
# print("Factorial of", num, "is" , fac(num),".")

# Method : 3
def fack(n):
    return 1 if (n==1 or n==0) else n * fack(n-1)

n = 5

print(fack(n))

    

# Define the function needed add, sub, mul, div
# print option to user
# ask for value
# call the function
# while loop to continue the program until the user wants to exit

def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def sub(a, b): 
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")

def mul(a, b): 
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")

def div(a, b): 
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")

while True:

     print("A : Addition")    
     print("B : Subtration")    
     print("C : Multiplication")    
     print("D : Division")   
     print("E : Exit") 

     choice = input("Input Your Choice: ")

     if choice == "a" or choice == "A":
           print("Addition")
           a = int(input("Input First Number: "))
           b = int(input("Input Second Number: "))
           add(a, b)
    
     elif choice == "b" or choice =="B": 
         print("Subtraction")

         a = int(input("Input First Number: "))
         b = int(input("Input Second Number: "))
         sub(a, b)

     elif choice == "c" or choice =="C":
         print("Multiplication")

         a = int(input("Input First Number: "))
         b = int(input("Input Second Number: "))
         mul(a, b)

     elif choice == "d" or choice =="D":
         print("Division")

         a = int(input("Input First Number: "))
         b = int(input("Input Second Number: "))
         div(a, b)


     elif choice == "e" or choice =="E":
         print("Program ended")

         quit()


        

    
    

    







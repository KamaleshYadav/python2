#Generate an infinite fibonnachi series by using generator

from re import A


def fibonachi():
    a,b = 0,1
    while True:
        yield a 
        a,b=b,a+b

f1 = fibonachi()  
print(next(f1))     
print(next(f1))     
print(next(f1))     
print(next(f1))     
print(next(f1))     
print(next(f1))     
# its list
# mybooks = ["Maths", "c", "Java"]

# mybooks[0] = "Python"
# print(mybooks)


# Tuple
mybooks = ("Maths", "c", "Java")
# print(type(mybooks))
# mybooks[0] = "Python"  its error q tuple does not change
# print(mybooks[0])
# del mybooks
# print(len(mybooks))

# Tuple can change indirectly
mybooksnew = list(mybooks)
print(mybooksnew)
mybooksnew[0]= "Python"

mybooks = tuple(mybooksnew)
print(mybooks)
# madam : this is palindrome

# Method 1 : 1) find reverse of string  2) Check if reverse and original are same or not

s = input("Enter a string :")

reverse = (s[::-1])

print(reverse)

if reverse == s:
    print(s,"is a palindrome")

else:
    print(s,"is not a palindrome")
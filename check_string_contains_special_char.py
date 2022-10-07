import re
str1 = "raj"
str = "welcome@@2To%%Python**Programming@!!^%%@$"

regex = re.compile('[@_!#$%^&*()<>?/\|{}~:]')

if(regex.search(str) == None):
    print("No special characters present in a string")
else:
    print("String contain special characters")


    
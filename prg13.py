string = input("Enter a string :")
start = string[0]
end = string[-1]
middle = string[1:-1]
newstring = end + middle + start
print(newstring)

string = input("Enter a string : ")
first = string[0]
length = len(string)
remaining = string[1:length]
print("First letter is ",first)
print("Replace every occurence of first letter with itself ")
newstring = remaining.replace(first,"$")
print(first + newstring)

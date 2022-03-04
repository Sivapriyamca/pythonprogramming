names = []
new = []
count = 0
size = int(input("Size of name list : "))
print("Enter names :")
for i in range(0,size):
    name = input()
    length=len(name)
    names.append(name)
for name in names:
        count = count + name.count("a")
print("Occurence of a in the list : ",count)

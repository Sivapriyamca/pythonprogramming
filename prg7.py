size = int(input("Size of the list : "))
integers = []
print("Enter the  values: ")
for i in range(0,size):
    value = int(input())
    integers.append(value)
for i in range(0,size):
    if(integers[i]>100):
        integers[i] = "over"
print(integers)


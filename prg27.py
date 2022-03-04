  list = []
n = int(input("size of list:"))
print("enter values: ")
for i in range(0,n):
    a = int(input())
    list.append(a)
print("the list is : ",list)
print("Sum of elements in the list is : ")
sum = 0
for i in range(0,n):
    sum = sum + list[i]
print(sum)

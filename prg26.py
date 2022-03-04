N = int(input("enter number:"))
l = []
first = 0
second= 1
print("fibonacci series is :")
for i in range(0, N):
    if (i == 0) or (i == 1):
          l.append(i)

    else:
         first = l[i-2]
         second = l[i-1]
         next = first + second
         l.append(next)

print(l)

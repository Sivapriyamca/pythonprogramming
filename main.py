import datetime
now = datetime.datetime.now()
currentyear =now.year
finalyear=int(input("Enter final year:"))
print("Leap years between {} and {} are".format(currentyear,finalyear))
for year in range(currentyear,finalyear):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0) :
        print(year)


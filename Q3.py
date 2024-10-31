year = int(input("Enter year : "))

if year % 4 == 0:
    print(year, "is leap year")
elif year % 4 != 0:
    print(year , "is not leap year")

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
    print("29 days")
else:
    print("Not a leap year")
    print("28 days")
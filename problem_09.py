# Determine  if  a year is a leap year ,(Leap years  are divisible by 4 , but not by 100 unless they are divisible by 400)

year = input("Enter a year you want to check: ")
year = int(year)


if (year % 400 == 0 )or(year % 4 == 0 and year % 100 != 0 ):
    print("The year is a leap year")
else:
    print("The year is not a leap year")
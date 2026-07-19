#accept a year and check if it ia a leap year or not 

a = int(input("Enter a year: "))

if a % 100 == 0 and a % 400 == 0:
    print("Leap year")
elif a % 100 !=0 and a % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")
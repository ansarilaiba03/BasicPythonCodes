#accept a number and check if it is a perfect number or not
# a number whose sum of factors is equal to the number itself
# eg 6 = 1,2,3 = 1+2+3 = 6

n = int(input("Enter a number: "))

sum = 0 

for i in range (1, n, 1):
    if n%i == 0:
        sum = sum + i

if sum == n:
    print("is a perfect number")
else:
    print("Not a perfect number")
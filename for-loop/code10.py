#check if a number is prime or not

n = int(input("Enter a number: "))
count=0
for i in range(2,n,1):
    if n%i==0:
        count = count + 1

if count == 0:
    print("prime number")
else:
    print("not a prime number")
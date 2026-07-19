#print the sum of all even and odd numbers in range separately

n = int(input("enter a number: "))

even = 0
odd = 0

for i in range (1, n+1, 1):
    if i%2==0:
        even = even + i
    else:
        odd = odd + i 

print(f"sum of even numbers: {even} and odd numbers : {odd}")


#accept a number and print its reverse
# 576
# (0*10 + 6) = 6
# (6*10 + 7) = 67
# (67*10 + 5) = 675
a = int(input("Enter a number: "))

rev = 0

while a > 0:
    rev = rev*10 + a%10 
    a = a // 10 

print(rev)

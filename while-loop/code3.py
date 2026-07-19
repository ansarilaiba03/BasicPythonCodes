# accept a number and check if it is a palindromic number 

a = int(input("Enter a number: "))
copy = a

rev = 0 

while a>0:
    rev = rev * 10 + a % 10
    a = a // 10

print(rev)

if rev==copy:
    print("palindrome")
else:
    print("not a plaindrome")
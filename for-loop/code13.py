# count all letters, digits, and special symbols from a given string 

a = "P@#yn26at^&i5ve"

letters = 0
digits = 0
special = 0

for i in a:
    if i.isdigit():
        digits+=1
    elif i.isalpha():
        letters+=1
    else:
        special+=1

print(f"letters : {letters}, digits: {digits}, special: {special}")
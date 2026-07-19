#accept number and age from the user. check if the user is a valid voter or not

name = input("enter you name: ")
age = int(input("enter your age: "))

if age >= 18:
    print(f"hello {name}, you are a valid voter")
else:
    print(f"hello {name}, you are an invalid voter")
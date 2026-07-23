'''
kwargs = key word arguments
prints a dictonary
'''
def information(**kwargs):
    print("Your information is: \n")
    for i in kwargs:
        print(f"{i}: {kwargs[i]}")

information(name = "laiba", age = 19, designation = "AI/ML")
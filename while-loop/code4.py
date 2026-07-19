#create a random number guessing game with python

import random #library for random number 

num = random.randint(1,100)
tries = 0

while True:
    a = int(input("guess the number: "))
    if a>num:
        tries +=1
        print("opps, guess a lesser number")
    elif a<num:
        tries +=1
        print("nope, guess a greater number")
    else:
        tries +=1
        print(f"yessssssss, you won, tries= {tries}")
        break


#write a python program to sum all the values in a dictionary

d = {10:100, 20:200, 30:300, 40:400}

sum = 0

for i in d:
    sum += d[i]

print(f"Sum = {sum}")


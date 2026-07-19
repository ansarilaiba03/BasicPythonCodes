#mean of list elements

a = [1,4,6,8,2,4]

sum = 0 

for i in a:
    sum = sum + i

avg = sum / len(a)
print(f"average: {avg}")
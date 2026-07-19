#print positive and negative numbers of a list

a = [1,4,5,-1,-2,6,-2,0]

print("positive numbers: ")
for i in a:
    if i<0:
        print(i)

print("negative numbers: ")
for i in a:
    if i>0:
        print(i)
#reverse a string without using in build functions

a = "laiba"
b = ""

# print(a[::-1]) 

#using for loop

for i in range(len(a)-1 ,-1 ,-1):
    b = b + a[i]

print(b)